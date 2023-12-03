
from payment.models import Payment
from rest_framework import viewsets
from payment.serializers import PaymentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class PaymentViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели платежа на основе ViewSet
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('well', 'lesson', 'payment_method',)
    ordering_fields = ('payment_data',)