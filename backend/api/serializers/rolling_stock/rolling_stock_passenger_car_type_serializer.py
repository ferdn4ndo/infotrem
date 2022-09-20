from rest_framework import serializers

from core.models import PassengerCarType


class RollingStockPassengerCarTypeSerializer(serializers.ModelSerializer):
    """Serializer for the PassengerCarType model"""

    class Meta:
        model = PassengerCarType
        fields = '__all__'
