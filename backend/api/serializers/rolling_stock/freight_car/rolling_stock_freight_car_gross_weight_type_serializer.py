from rest_framework import serializers

from core.models import FreightCarGrossWeightType


class RollingStockFreightCarGrossWeightTypeSerializer(serializers.ModelSerializer):
    """Serializer for the FreightCarGrossWeightType model"""

    class Meta:
        model = FreightCarGrossWeightType
        fields = '__all__'
