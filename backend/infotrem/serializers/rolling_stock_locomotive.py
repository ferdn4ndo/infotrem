import re
from typing import Optional

from rest_framework import serializers

from infotrem.models.rolling_stock import RollingStock
from infotrem.models.rolling_stock_locomotive import RollingStockLocomotiveModel, RollingStockLocomotive


class RollingStockLocomotiveModelSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockLocomotiveModel model"""

    class Meta:
        model = RollingStockLocomotiveModel
        excludes = ['rolling_stock']


class RollingStockLocomotiveSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockLocomotive model"""
    model = RollingStockLocomotiveModelSerializer()

    class Meta:
        model = RollingStockLocomotive
        excludes = ['rolling_stock']

    @staticmethod
    def parse_model_from_name(name: str) -> Optional[RollingStockLocomotiveModel]:
        name = name.upper().replace(" ", "_").replace("-", "_")
        parts = re.sub("_+", "_", name).split("_")
        for part in parts:
            models = RollingStockLocomotiveModel.objects.filter(name=part)
            if len(models) > 0:
                return models[0]

        return None

    @staticmethod
    def create_from_name(name: str, rolling_stock: RollingStock) -> Optional[RollingStockLocomotive]:
        """
        Creates a rolling stock locomotive from a given name. Some examples:

        G22U - 4314
        U20C 3210
        G12_4200

        :param rolling_stock:
        :param name:
        :return:
        """
        model = RollingStockLocomotiveSerializer.parse_model_from_name(name)

        if model is None:
            return None

        rolling_stock = RollingStockLocomotive(
            rolling_stock=rolling_stock,
            model=model,
            horsepower_total=model.horsepower_total if model is not None else None,
            horsepower_available=model.horsepower_available if model is not None else None,
            first_operation_year=None,
            aar_wheel_arrangement=model.aar_wheel_arrangement if model is not None else None,
            whyte_wheel_arrangement=model.whyte_wheel_arrangement if model is not None else None,
            tank_total_liters=model.tank_total_liters if model is not None else None,
            primary_motor=model.primary_motor if model is not None else None,
            traction_motor=model.traction_motor if model is not None else None,
            serial_number=None,
        )
        rolling_stock.save()

        return rolling_stock
