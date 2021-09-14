from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

#from django.conf import settings
#from user.models import User


#User = settings.AUTH_USER_MODEL
User = get_user_model()

# Create your models here.

class Categories(models.Model):
    name = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name



class Genres(models.Model):
    name = models.TextField()
    slug = models.SlugField(max_length=20, )
    #categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='genres')

    def __str__(self):
        return self.name



class Titles(models.Model):
    name = models.TextField()
    year = models.PositiveIntegerField(null=False)
    #IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2022)])
    #TODO зависемость от всех оценок и определение среднего значения
    #rating = models.FloatField(null=True)
    #description = models.TextField()
    #genre = models.ManyToManyField(Genres, ) # model Genre_Title 
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Reviews(models.Model):
    titles = models.ForeignKey(Titles, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(db_column='text',db_tablespace='text', blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        blank=False,
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв на {self.titles}'



class Comments(models.Model):
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Коментарий {self.author} "


class Genre_Title(models.Model):
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        return f'Сопостовление {self.title}'
    