from rest_framework import serializers

from demo.models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'user', 'text', 'created_at', 'opened']
