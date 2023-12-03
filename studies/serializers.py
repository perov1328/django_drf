
from rest_framework import serializers
from studies.models import Well, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Урока
    """
    class Meta:
        model = Lesson
        fields = ('well', 'title', 'description', 'video',)

class WellSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Курса
    """
    count_lessons = serializers.IntegerField(source='lesson_set.all.count')
    lessons = LessonSerializer(source='lesson_set', many=True)
    class Meta:
        model = Well
        fields = ('title', 'preview', 'description', 'count_lessons', 'lessons',)
