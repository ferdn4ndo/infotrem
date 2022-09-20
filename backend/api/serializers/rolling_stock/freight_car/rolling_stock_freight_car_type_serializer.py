from rest_framework import serializers

from api.serializers.rolling_stock.freight_car.rolling_stock_freight_car_category_serializer import RollingStockFreightCarCategorySerializer
from core.models import FreightCarType


class RollingStockFreightCarTypeSerializer(serializers.ModelSerializer):
    """Serializer for the FreightCarType model"""
    category = RollingStockFreightCarCategorySerializer()

    class Meta:
        model = FreightCarType
        fields = '__all__'
