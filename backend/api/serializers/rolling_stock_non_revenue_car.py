from rest_framework import serializers

from api.models.non_revenue_car_model import NonRevenueCarType, NonRevenueCar


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
