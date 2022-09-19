from rest_framework import serializers

from core.models.passenger_car.passenger_car_material_model import PassengerCarMaterial
from core.models.passenger_car.passenger_car_model import PassengerCar
from core.models.passenger_car.passenger_car_type_model import PassengerCarType


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
    material = RollingStockPassengerCarMaterialSerializer()
    type = RollingStockPassengerCarTypeSerializer()

    class Meta:
        model = PassengerCar
        excludes = ['rolling_stock']
