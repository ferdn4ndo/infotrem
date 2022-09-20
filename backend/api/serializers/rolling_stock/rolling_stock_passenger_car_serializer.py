from rest_framework import serializers

from api.serializers.rolling_stock.rolling_stock_passenger_car_material_serializer import \
    RollingStockPassengerCarMaterialSerializer
from api.serializers.rolling_stock.rolling_stock_passenger_car_type_serializer import \
    RollingStockPassengerCarTypeSerializer
from core.models import PassengerCar


class RollingStockPassengerCarSerializer(serializers.ModelSerializer):
    """Serializer for the PassengerCar model"""
    material = RollingStockPassengerCarMaterialSerializer()
    type = RollingStockPassengerCarTypeSerializer()

    class Meta:
        model = PassengerCar
        excludes = ['rolling_stock']
