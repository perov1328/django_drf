from studies.models import Well
from rest_framework import viewsets
from studies.serializers import WellSerializer
from studies.permissions import IsAuthor, IsModerator
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from studies.paginators import StudiesPaginator
from studies.tasks import send_update_info
from subscription.models import Subscription
from rest_framework.response import Response


class WellViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Курса на основе ViewSets
    """
    queryset = Well.objects.all()
    serializer_class = WellSerializer
    pagination_class = StudiesPaginator

    def get_permissions(self):
        """
        Права доступа
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAdminUser, IsModerator, IsAuthor]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser, IsAuthor]
        elif self.action == 'update':
            permission_classes = [IsAdminUser, IsAuthor]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        """
        Метод для обновления курса
        """
        serializer.save()
        pk = self.kwargs.get('pk')
        well = Well.objects.get(pk=pk)
        subscription = Subscription.objects.filter(well=well, is_active=True)
        emails = list(subscription.values_list('user__email', flat=True))

        send_update_info.delay(emails)
        return Response('Messages sent.')
