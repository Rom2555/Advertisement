from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from demo.models import Advertisement
from demo.permissions import IsOwnerOrReadOnly
from demo.serializers import AdvertisementSerializer


class CustomUserRateThrottle(UserRateThrottle):
    rate = '10/min'


class CustomAnonRateThrottle(AnonRateThrottle):
    rate = '2/min'


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]
    throttle_classes = [CustomUserRateThrottle, CustomAnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
