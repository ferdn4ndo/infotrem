from rest_framework import serializers

from core.models import FreightCarCategory


class RollingStockFreightCarCategorySerializer(serializers.ModelSerializer):
    """Serializer for the FreightCarCategory model"""

    class Meta:
        model = FreightCarCategory
        fields = '__all__'
