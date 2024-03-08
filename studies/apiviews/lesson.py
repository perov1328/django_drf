
from studies.models import Lesson
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from studies.serializers import LessonSerializer
from studies.permissions import IsAuthor, IsModerator
from rest_framework.permissions import IsAdminUser
from studies.paginators import StudiesPaginator


class LessonCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущности модели Урока
    """
    serializer_class = LessonSerializer



class LessonListAPIView(ListAPIView):
    """
    Контроллер для просмотра списка сущностей модели Урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = StudiesPaginator


class LessonRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотра конкретной сущности модели Урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsAdminUser, IsModerator, IsAuthor]


class LessonUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsModerator, IsAuthor]


class LessonDestroyAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsAdminUser, IsAuthor]
