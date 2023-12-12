
from rest_framework.generics import CreateAPIView, DestroyAPIView
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializers
from studies.models import Well
from rest_framework.permissions import IsAuthenticated


class SubscriptionCreateAPIView(CreateAPIView):
    """
    Контроллер для создания подписки
    """
    serializer_class = SubscriptionSerializers
    permission_classes = [IsAuthenticated]


class SubscriptionDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления подписки
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers
    permission_classes = [IsAuthenticated]