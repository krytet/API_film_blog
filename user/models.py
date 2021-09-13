from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ROLES_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=10, choices=ROLES_CHOICES, default='user')
    email = models.EmailField(blank=False, unique=True, verbose_name='email adress', db_column='email')
    description = models.TextField(blank=True)
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
        #null=True,
    )
    