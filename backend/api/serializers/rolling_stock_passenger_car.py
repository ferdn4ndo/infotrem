from rest_framework import serializers

from api.models.passenger_car_model import \
    PassengerCarMaterial, \
    PassengerCarType, \
    PassengerCar

from api.serializers.rolling_stock_freight_car import \
    RollingStockFreightCarTypeSerializer


class RollingStockPassengerCarMaterialSerializer(serializers.ModelSerializer):
    """Serializer for the PassengerCarMaterial model"""

    class Meta:
        model = PassengerCarMaterial
        fields = '__all__'


class RollingStockPassengerCarTypeSerializer(serializers.ModelSerializer):
    """Serializer for the PassengerCarType model"""

    class Meta:
        model = PassengerCarType
        fields = '__all__'


class RollingStockPassengerCarSerializer(serializers.ModelSerializer):
    """Serializer for the PassengerCar model"""
    material = RollingStockPassengerCarTypeSerializer()
    type = RollingStockFreightCarTypeSerializer()

    class Meta:
        model = PassengerCar
        excludes = ['rolling_stock']
