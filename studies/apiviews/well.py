
from studies.models import Well
from rest_framework import viewsets
from studies.serializers import WellSerializer


class WellViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Курса на основе ViewSets
    """
    queryset = Well.objects.all()
    serializer_class = WellSerializer
