from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import serializers

from . import models
from .parser import CurrentReview_id, CurrentTitle_id

User = get_user_model()


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Categories


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Genres


class TitlesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    category = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()


    class Meta:
        fields = "__all__"
        model = models.Titles

    def get_rating(self, obj):
        soure_list = obj.reviews.all()

        if len(soure_list) != 0:
            rating = 0
            for i in soure_list:
                rating += i.score
            rating = float(rating) / float(len(soure_list))
            return rating
        return 0

    def get_genre(self, obj):
        genres = get_list_or_404(models.Genre_Title, title_id=obj.id)
        genre_list = []
        for genre in genres:
            genre_list.append(get_object_or_404(models.Genres, id=genre.genre_id))
        serializer = GenresSerializer(genre_list, many=True)
        return serializer.data

    def get_category(self, obj):
        category = obj.category
        serializer = CategoriesSerializer(category)
        return serializer.data




class ReviewsSerializer(serializers.ModelSerializer):
    titles = serializers.HiddenField(default=CurrentTitle_id())
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        fields = "__all__"
        model = models.Reviews


class CommentsSerializer(serializers.ModelSerializer):
    reviews = serializers.HiddenField(default=CurrentReview_id())
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        fields = "__all__"
        model = models.Comments


class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='description', required=False)
    email = serializers.EmailField(
        required=True
    )
    role = serializers.ChoiceField(
        choices=['user', 'moderator', 'admin'],
        default='user',
    )

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role')
        model = User