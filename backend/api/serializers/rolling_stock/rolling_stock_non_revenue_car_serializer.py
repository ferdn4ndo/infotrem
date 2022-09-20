from rest_framework import serializers

from api.serializers.rolling_stock.rolling_stock_non_revenue_car_type_serializer import \
    RollingStockNonRevenueCarTypeSerializer
from core.models import NonRevenueCar


class RollingStockNonRevenueCarSerializer(serializers.ModelSerializer):
    """Serializer for the NonRevenueCar model"""
    type = RollingStockNonRevenueCarTypeSerializer()

    class Meta:
        model = NonRevenueCar
        excludes = ['rolling_stock']
