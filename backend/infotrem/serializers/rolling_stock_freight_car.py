import re
from typing import Optional, Tuple

from rest_framework import serializers

from infotrem.models.location import TrackGaugeConfiguration
from infotrem.models.rolling_stock_freight_car import \
    RollingStockFreightCarCategory, \
    RollingStockFreightCarGrossWeightType, \
    RollingStockFreightCarType,\
    RollingStockFreightCar
from infotrem.models.rolling_stock import RollingStock
from infotrem.services.strings import break_string_into_words


class RollingStockFreightCarCategorySerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockFreightCarCategory model"""

    class Meta:
        model = RollingStockFreightCarCategory
        fields = '__all__'


class RollingStockFreightCarGrossWeightTypeSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockFreightCarGrossWeightType model"""

    class Meta:
        model = RollingStockFreightCarGrossWeightType
        fields = '__all__'


class RollingStockFreightCarTypeSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockFreightCarType model"""
    category = RollingStockFreightCarCategorySerializer()

    class Meta:
        model = RollingStockFreightCarType
        fields = '__all__'


class RollingStockFreightCarSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockFreightCar model"""
    model_type = RollingStockFreightCarTypeSerializer()
    gross_weight_type = RollingStockFreightCarGrossWeightTypeSerializer()

    class Meta:
        model = RollingStockFreightCar
        excludes = ['rolling_stock']

    @staticmethod
    def parse_gauge_from_name(name: str) -> Optional[TrackGaugeConfiguration]:
        name_parts = break_string_into_words(name)

        for part in name_parts:
            if re.match(r"^[A-Z]{3}$", part):
                model = RollingStockFreightCarSerializer.parse_model_from_name(name)
                if model is not None:
                    return model[1].gauge

        return None

    @staticmethod
    def parse_model_from_name(name: str) -> Optional[Tuple]:
        name_parts = break_string_into_words(name)

        for part in name_parts:
            if re.match(r"^[A-Z]{3}$", part):
                sigo_model = re.match(r"", part)[0]
                category = RollingStockFreightCarType.objects.filter(letters=sigo_model[:2])
                if len(category) == 0:
                    continue

                gross_weight_type = RollingStockFreightCarGrossWeightType.objects.filter(letter=sigo_model[2:])
                if len(gross_weight_type) == 0:
                    continue

                return category[0], gross_weight_type[0]

        return None

    @staticmethod
    def create_from_name(name: str, rolling_stock: RollingStock) -> Optional[RollingStockFreightCar]:
        """
        Creates a rolling stock locomotive from a given name. Some examples:

        TSR 036017-1
        TCD_048052-5

        :param rolling_stock:
        :param name:
        :return:
        """
        model = RollingStockFreightCarSerializer.parse_model_from_name(name)

        if model is None:
            return None

        rolling_stock = RollingStockFreightCar(
            rolling_stock=rolling_stock,
            model_type=model[0],
            gross_weight_type=model[1],
        )
        rolling_stock.save()

        return rolling_stock
