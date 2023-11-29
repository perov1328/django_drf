
from rest_framework import serializers
from studies.models import Well, Lesson


class WellSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Курса
    """
    class Meta:
        model = Well
        fields = ('title', 'preview', 'description',)


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Урока
    """
    class Meta:
        model = Lesson
        fields = ('title', 'description', 'preview', 'video',)
