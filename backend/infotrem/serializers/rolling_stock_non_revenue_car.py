from rest_framework import serializers

from infotrem.models.rolling_stock_non_revenue_car import RollingStockNonRevenueCarType, RollingStockNonRevenueCar


class RollingStockNonRevenueCarTypeSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockNonRevenueCarMaterial model"""

    class Meta:
        model = RollingStockNonRevenueCarType
        fields = '__all__'


class RollingStockNonRevenueCarSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockNonRevenueCar model"""
    type = RollingStockNonRevenueCarTypeSerializer()

    class Meta:
        model = RollingStockNonRevenueCar
        excludes = ['rolling_stock']
