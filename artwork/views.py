from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
import requests
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

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


class Profile(RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        queryset = self.request.user
        return queryset


class Registration(CreateAPIView):
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        if request.POST['email'] not in User.objects.values_list('email'):
            password = User.objects.make_random_password()
            username = request.POST['email'].split('@')[0]
            profile = {
                'username' : username,
                'email' : request.POST['email'],
            }
            serializer = serializers.UserSerializer(data=profile)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = get_object_or_404(User, username=username)
            user.set_password(password)
            user.save()
            post_data = {
                'username' : username,
                'password' : password,
            }
            #TODO отпредоктировать ссылку на token_obtain_pair
            url = requests.post('http://127.0.0.1:8000/api/v1/auth/token/', data=post_data)
            token = url.json()['access']
            text = f"Добро пожаловать на наш сервис. Ваш токен для авторизации : {token}" 
            send_mail(
                'Регистрация на сайте YaMDb',
                text,
                'from@YaMDb.ru',  # Это поле "От кого"
                [request.POST['email']],  # Это поле "Кому" (можно указать список адресов)
                fail_silently=False, # Сообщать об ошибках («молчать ли об ошибках?»)
            )
            serialize = serializers.RegisterSerializer(profile)
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        



    





