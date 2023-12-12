
from rest_framework import serializers
from subscription.models import Subscription


class SubscriptionSerializers(serializers.ModelSerializer):
    """
    Сериализатор для модели подписки
    """
    class Meta:
        model = Subscription
        fields = ('id', 'well',)
