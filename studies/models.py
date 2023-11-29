
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Well(models.Model):
    """
    Модель для курса
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='studies', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

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
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='studies', verbose_name='Превью', **NULLABLE)
    video = models.CharField(max_length=250, verbose_name='Ссылка на видео')

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
