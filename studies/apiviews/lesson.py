
from studies.models import Lesson
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from studies.serializers import LessonSerializer


class LessonCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущности модели Урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(ListAPIView):
    """
    Контроллер для просмотра списка сущностей модели Урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотра конкретной сущности модели Урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
