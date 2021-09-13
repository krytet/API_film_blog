from rest_framework import serializers
from .models import (
    Categories,
    Genres,
    Titles,
    Reviws,
    Comments)

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Categories


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Genres


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Titles


class ReviwsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Reviws


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Comments