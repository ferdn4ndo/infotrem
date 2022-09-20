from rest_framework import serializers

from core.models import NonRevenueCarType


class RollingStockNonRevenueCarTypeSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockNonRevenueCarMaterial model"""

    class Meta:
        model = NonRevenueCarType
        fields = '__all__'
