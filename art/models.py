from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

#from django.contrib.auth import get_user_model
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.

class Categories(models.Model):
    name = models.TextField()
    slug = models.SlugField()



class Genres(models.Model):
    name = models.TextField()
    slug = models.SlugField(max_length=20)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='genres')



class Titles(models.Model):
    name = models.TextField()
    year = models.IntegerField(
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(2022)
        ]
    )
    #TODO зависемость от всех оценок и определение среднего значения
    rating = models.FloatField(null=True)
    description = models.TextField()
    genre = models.ManyToManyField(Genres, )
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    


class Reviws(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviws')
    titles = models.ForeignKey(Titles, on_delete=models.CASCADE, related_name='reviws')
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField(auto_now_add=True)



class Comments(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    reviws = models.ForeignKey(Reviws, on_delete=models.CASCADE, related_name='commets')
    pub_date = models.DateTimeField(auto_now_add=True)


