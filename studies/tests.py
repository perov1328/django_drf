
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from studies.models import Well, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        """
        Создание тестовой модели пользователя, курса и урока
        """
        self.user = User.objects.create(
            email='test@yandex.ru',
            password='test'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.well = Well.objects.create(
            title='test',
            description='test'
        )

        self.lesson = Lesson.objects.create(
            title='test',
            description='test',
            well=self.well
        )

    def test_get_list(self):
        """
        Тестирование вывода всех уроков
        """
        response = self.client.get(reverse('studies:lesson_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        data = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': 1,
                        'well': 1,
                        'title': 'test',
                        'description': 'test',
                        'video': '',
                        'author': None}
                ]
        }

        self.assertEqual(
            response.json(),
            data
        )

    def test_lesson_create(self):
        """
        Тестирование создания нового урока
        """
        data = {
            "well": self.well.pk,
            "title": "test 1",
            "description": "test 1",
            "video": "https://www.youtube.com/test1"
        }

        response = self.client.post(
            reverse('studies:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_create_validate_error(self):
        """
        Тестирование создания нового урока с ошибкой в ссылке на видео (не с платформы youtube)
        """
        data = {
            "well": self.well.pk,
            "title": "test 2",
            "description": "test 2",
            "video": "https://www.rutube.com/test2",
            "author": self.user.pk
        }

        response = self.client.post(
            reverse('studies:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            1
        )

    def test_lesson_detail(self):
        """
        Тестирование для вывода информации о конкретном урока
        """
        retrive_url = reverse('studies:lesson_detail', args=[self.lesson.pk])
        response = self.client.get(retrive_url)

        print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        data = {
            'id': 5,
            'well': 4,
            'title': 'test',
            'description': 'test',
            'video': '',
            'author': None
        }

        self.assertEqual(
            response.json(),
            data
        )

    def test_lesson_update(self):
        """
        Тестирование для обновления информации по уроку
        :return:
        """
        update_url = reverse('studies:lesson_update', args=[self.lesson.pk])
        update_data = {
            "title": "test 123",
            "video": "https://www.youtube.com/test_123"
        }
        response = self.client.patch(update_url, update_data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(self.lesson.title, update_data['title'])
        self.assertEqual(self.lesson.video, update_data['video'])

    def test_lesson_delete(self):
        """
        Тестирование для удаления урока
        """
        delete_url = reverse('studies:lesson_delete', args=[self.lesson.pk])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())
