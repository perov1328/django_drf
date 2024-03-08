
from rest_framework import serializers
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели платежа
    """
    class Meta:
        model = Payment
        fields = ('user', 'payment_data', 'well', 'lesson', 'payment_sum', 'payment_method',)
