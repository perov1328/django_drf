from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from subscription.models import Subscription
from users.models import User
from studies.models import Well


class SubscriptionTestCase(APITestCase):
    """
    Тестирование модели подписки
    """

    def setUp(self):
        """
        Создание тестовой модели пользователя, курса и подписки
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

        self.subscription = Subscription.objects.create(
            user=self.user,
            well=self.well
        )

    def test_subscription_create(self):
        """
        Тестирование создания подписки
        """
        data = {
            "user": self.user.pk,
            "well": self.well.pk
        }

        response = self.client.post(
            reverse('subscription:subscription_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Subscription.objects.all().count(),
            2
        )

    def test_subscription_delete(self):
        """
        Тестирование удаления подписки
        """
        delete_url = reverse('subscription:subscription_delete', args=[self.subscription.pk])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subscription.objects.filter(id=self.subscription.pk).exists())
