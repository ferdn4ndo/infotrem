import re
from typing import Optional, Tuple

from rest_framework import serializers

from api.serializers.rolling_stock.freight_car.rolling_stock_freight_car_gross_weight_type_serializer import \
    RollingStockFreightCarGrossWeightTypeSerializer
from api.serializers.rolling_stock.freight_car.rolling_stock_freight_car_type_serializer import RollingStockFreightCarTypeSerializer
from core.models import FreightCar, TrackGauge, FreightCarType, FreightCarGrossWeightType, RollingStock
from core.services.strings.strings_service import StringsService


class RollingStockFreightCarSerializer(serializers.ModelSerializer):
    """Serializer for the FreightCar model"""
    model_type = RollingStockFreightCarTypeSerializer()
    gross_weight_type = RollingStockFreightCarGrossWeightTypeSerializer()

    class Meta:
        model = FreightCar
        excludes = ['rolling_stock']

    @staticmethod
    def parse_gauge_from_name(name: str) -> Optional[TrackGauge]:
        name_parts = StringsService(input_string=name).break_string_into_words()

        for part in name_parts:
            if re.match(r"^[A-Z]{3}$", part):
                model = RollingStockFreightCarSerializer.parse_model_from_name(name)
                if model is not None:
                    return model[1].gauge

        return None

    @staticmethod
    def parse_model_from_name(name: str) -> Optional[Tuple]:
        name_parts = StringsService(input_string=name).break_string_into_words()

        for part in name_parts:
            if re.match(r"^[A-Z]{3}$", part):
                sigo_model = re.match(r"", part)[0]
                category = FreightCarType.objects.filter(letters=sigo_model[:2])
                if len(category) == 0:
                    continue

                gross_weight_type = FreightCarGrossWeightType.objects.filter(letter=sigo_model[2:])
                if len(gross_weight_type) == 0:
                    continue

                return category[0], gross_weight_type[0]

        return None

    @staticmethod
    def create_from_name(name: str, rolling_stock: RollingStock) -> Optional[FreightCar]:
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

        rolling_stock = FreightCar(
            rolling_stock=rolling_stock,
            model_type=model[0],
            gross_weight_type=model[1],
        )
        rolling_stock.save()

        return rolling_stock
