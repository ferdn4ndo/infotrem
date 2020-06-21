from rest_framework import serializers

from infotrem.models.rolling_stock_passenger_car import \
    RollingStockPassengerCarMaterial, \
    RollingStockPassengerCarType, \
    RollingStockPassengerCar

from infotrem.serializers.rolling_stock_freight_car import \
    RollingStockFreightCarTypeSerializer


class RollingStockPassengerCarMaterialSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockPassengerCarMaterial model"""

    class Meta:
        model = RollingStockPassengerCarMaterial
        fields = '__all__'


class RollingStockPassengerCarTypeSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockPassengerCarType model"""

    class Meta:
        model = RollingStockPassengerCarType
        fields = '__all__'


class RollingStockPassengerCarSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockPassengerCar model"""
    material = RollingStockPassengerCarTypeSerializer()
    type = RollingStockFreightCarTypeSerializer()

    class Meta:
        model = RollingStockPassengerCar
        excludes = ['rolling_stock']
