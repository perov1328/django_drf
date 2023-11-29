
from django.urls import path
from studies.apps import StudiesConfig
from rest_framework.routers import DefaultRouter
from studies.views.well import WellViewSet
from studies.views.lesson import *

app_name = StudiesConfig.name

router = DefaultRouter()
router.register(r'well', WellViewSet, basename='well')


urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('create/lesson', CreateAPIView.as_view(), name='lesson_create'),
    path('detail/lesson/<int:pk>', RetrieveAPIView.as_view(), name='lesson_detail'),
    path('update/lesson/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('delete/lesson/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete')
] + router.urls