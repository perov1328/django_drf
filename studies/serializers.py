
from rest_framework import serializers
from studies.models import Well, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Урока
    """
    class Meta:
        model = Lesson
        fields = ('id', 'well', 'title', 'description', 'video', 'author',)


class WellSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Курса
    """
    count_lessons = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    class Meta:
        model = Well
        fields = ('id', 'title', 'preview', 'description', 'count_lessons', 'lessons', 'author',)
