from django.contrib.auth import get_user_model
from django.http import request
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from . import models, permissions, serializers

User = get_user_model()


class CategoriesViewSet(ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)
    lookup_field = 'slug'


class GenresViewSet(ModelViewSet):
    queryset = models.Genres.objects.all()
    serializer_class = serializers.GenresSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)
    lookup_field = 'slug'


class TitlesViewSet(ModelViewSet):
    queryset = models.Titles.objects.all()
    serializer_class = serializers.TitlesSerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['category__slug', 'genre_title__genre__slug', 'name', 'year']


class ReviewsViewSet(ModelViewSet):
    serializer_class = serializers.ReviewsSerializer
    permission_classes = [permissions.IsAuthorOrModeratorOrReadOnly, ]

    def get_queryset(self):
        #review = models.Reviews.objects.filter(titles_id=self.kwargs['title_id'])
        title = get_object_or_404(models.Titles, pk=self.kwargs['title_id'])
        return title.reviews.all()


    def perform_create(self, serializer):
        title = get_object_or_404(models.Titles, pk=self.kwargs['title_id'])
        return serializer.save(author=self.request.user, titles=title)


class CommentsViewSet(ModelViewSet):
    #queryset = models.Comments.objects.all()
    serializer_class = serializers.CommentsSerializer

    def get_queryset(self):
        title = get_object_or_404(models.Titles, pk=self.kwargs['title_id'])
        review = get_object_or_404(models.Reviews, titles=title, pk=self.kwargs['review_id'])
        return review.comments.all()

    def perform_create(self, serializer):
        title = get_object_or_404(models.Titles, pk=self.kwargs['title_id'])
        review = get_object_or_404(models.Reviews, titles=title, pk=self.kwargs['review_id'])
        return serializer.save(author=self.request.user, reviews=review)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.IsAdmin,)



