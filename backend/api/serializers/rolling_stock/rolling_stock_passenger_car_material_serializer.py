from rest_framework import serializers

from core.models import PassengerCarMaterial


class RollingStockPassengerCarMaterialSerializer(serializers.ModelSerializer):
    """Serializer for the PassengerCarMaterial model"""

    class Meta:
        model = PassengerCarMaterial
        fields = '__all__'
