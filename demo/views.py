from rest_framework.viewsets import ModelViewSet

from demo.models import Advertisement
from demo.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
