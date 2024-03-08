
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}


USER_ROLE = [
    ('User', 'User'),    # Пользователь
    ('Moderator', 'Moderator')    # Модератор
]


class User(AbstractUser):
    """
    Модель для пользователя
    """
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    job_title = models.CharField(max_length=15, choices=USER_ROLE, default='User')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
