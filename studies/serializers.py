
from rest_framework import serializers
from studies.models import Well, Lesson
from studies.validators import VideoValidator
from subscription.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Урока
    """
    class Meta:
        model = Lesson
        fields = ('id', 'well', 'title', 'description', 'video', 'author',)
        validators = [VideoValidator(field='video')]

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            user = self.context['request'].user
            lesson = Lesson.objects.create(author=user, **validated_data)
        else:
            lesson = Lesson.objects.create(**validated_data)
        return lesson


class WellSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Курса
    """
    count_lessons = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    is_subscription = serializers.SerializerMethodField()

    def get_is_subscription(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, well=obj, is_active=True).exists()
        return False

    class Meta:
        model = Well
        fields = ('id', 'title', 'preview', 'description', 'count_lessons', 'lessons', 'author', 'is_subscription')
