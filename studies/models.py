
from django.db import models
from users.models import User
from config import settings


NULLABLE = {'blank': True, 'null': True}


class Well(models.Model):
    """
    Модель для курса
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='studies', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Создатель курса')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return {self.title}

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """
    Модель урока
    """
    well = models.ForeignKey(Well, on_delete=models.CASCADE, **NULLABLE)
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='studies', verbose_name='Превью', **NULLABLE)
    video = models.CharField(max_length=250, verbose_name='Ссылка на видео')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Создатель урока')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return {self.title}

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
