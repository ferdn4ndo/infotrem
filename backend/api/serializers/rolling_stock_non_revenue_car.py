from rest_framework import serializers

from core.models.non_revenue_car.non_revenue_car_model import NonRevenueCar
from core.models.non_revenue_car.non_revenue_car_type_model import NonRevenueCarType


class RollingStockNonRevenueCarTypeSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockNonRevenueCarMaterial model"""

    class Meta:
        model = NonRevenueCarType
        fields = '__all__'


class RollingStockNonRevenueCarSerializer(serializers.ModelSerializer):
    """Serializer for the NonRevenueCar model"""
    type = RollingStockNonRevenueCarTypeSerializer()

    class Meta:
        model = NonRevenueCar
        excludes = ['rolling_stock']
