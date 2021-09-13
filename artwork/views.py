from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    GenresSerializer,
    ReviwsSerializer,
    TitlesSerializer,
    CommentsSerializer,
    CategoriesSerializer)

from .models import (
    Categories,
    Genres,
    Titles,
    Reviws,
    Comments,
    Genre_Title)



class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class GenresViewSet(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class TitlesViewSet(ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer


class ReviwsViewSet(ModelViewSet):
    queryset = Reviws.objects.all()
    serializer_class = ReviwsSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


