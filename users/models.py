from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ROLES_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=10, choices=ROLES_CHOICES)
    email = models.EmailField(blank=False, unique=True, verbose_name='email adress')
    