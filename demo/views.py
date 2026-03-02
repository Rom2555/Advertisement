from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from demo.models import Advertisement
from demo.permissions import IsOwnerOrReadOnly
from demo.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
