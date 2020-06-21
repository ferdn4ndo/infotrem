import re
from typing import Optional

from rest_framework import serializers

from infotrem.models.rolling_stock_freight_car import RollingStockFreightCar
from infotrem.models.rolling_stock_locomotive import RollingStockLocomotive
from infotrem.models.rolling_stock_non_revenue_car import RollingStockNonRevenueCar
from infotrem.models.rolling_stock_passenger_car import RollingStockPassengerCar
from infotrem.models.rolling_stock import RollingStockSigoRegional, RollingStock
from infotrem.models.track_gauge import TrackGauge
from infotrem.serializers.railroad import RailroadCompanySerializer, ManufacturerSerializer
from infotrem.serializers.rolling_stock_freight_car import RollingStockFreightCarSerializer
from infotrem.serializers.rolling_stock_locomotive import RollingStockLocomotiveSerializer
from infotrem.serializers.rolling_stock_non_revenue_car import RollingStockNonRevenueCarSerializer
from infotrem.serializers.rolling_stock_passenger_car import RollingStockPassengerCarSerializer
from infotrem.serializers.track_gauge import TrackGaugeSerializer
from infotrem.services.strings import break_string_into_words


class RollingStockSigoRegionalSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStockSigoRegional model"""
    original_company = RailroadCompanySerializer(required=False)

    class Meta:
        model = RollingStockSigoRegional
        fields = '__all__'


class RollingStockSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStock model"""
    gauge = TrackGaugeSerializer()
    regional = RollingStockSigoRegionalSerializer()
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = RollingStock
        fields = '__all__'

    @staticmethod
    def read_metadata(instance: RollingStock):
        types = RollingStock.RollingStockType
        types_map = {
            str(types.LOCOMOTIVE): (RollingStockLocomotive, RollingStockLocomotiveSerializer),
            str(types.FREIGHT_CAR): (RollingStockFreightCar, RollingStockFreightCarSerializer),
            str(types.PASSENGER_CAR): (RollingStockPassengerCar, RollingStockPassengerCarSerializer),
            str(types.NON_REVENUE_CAR): (RollingStockNonRevenueCar, RollingStockNonRevenueCarSerializer),
        }

        if instance.type not in types_map:
            return None

        try:
            model = types_map[instance.type][0]
            serializer = types_map[instance.type][1]
            rolling_stock = model.objects.get(pk=instance.rolling_stock_id)
            return serializer(rolling_stock).data
        except RollingStock.DoesNotExist:
            return None

    @staticmethod
    def parse_gauge_from_freight_car(name: str) -> Optional[TrackGauge]:
        name_parts = break_string_into_words(name)

        for part in name_parts:
            if re.match(r"^[A-Z]{3}$", part):
                model = RollingStockFreightCarSerializer.parse_model_from_name(name)
                if model is not None:
                    return model[1].gauge

        return None

    @staticmethod
    def get_sigo_number_from_name(name: str) -> Optional[int]:
        name_parts = break_string_into_words(name)
        sigo_number = None

        for part in name_parts:
            if re.match(r"^\d{6}-\d[A-Z]?$", part):
                sigo_number = int(str(re.match(r"", part)[0])[:6])
            if re.match(r"^\d{6}$", part):
                sigo_number = int(str(re.match(r"", part)[0]))

        return sigo_number

    @staticmethod
    def get_regional(name: str) -> Optional[RollingStockSigoRegional]:
        name_parts = break_string_into_words(name)

        for part in name_parts:
            if re.match(r"^\d{4:6}-\d[A-Z]?$", part):
                regional_letter = str(re.match(r"", part)[0])[-1:]
                regional = RollingStockSigoRegional.objects.find(letter=regional_letter)
                if len(regional) > 0:
                    return regional[0]

        return None

    @staticmethod
    def get_by_sigo(sigo_number):
        if sigo_number is None:
            return None

        sigo_number = int(sigo_number)
        try:
            return RollingStock.objects.get(sigo_number=sigo_number)
        except RollingStock.DoesNotExist:
            return None

    @staticmethod
    def get_or_create_from_name_and_type(name: str, car_type: RollingStock.RollingStockType) -> RollingStock:
        sigo_number = RollingStockSerializer.get_sigo_number_from_name(name)
        rolling_stock = RollingStockSerializer.get_by_sigo(sigo_number)

        if rolling_stock is None:
            is_freight_car = car_type == RollingStock.RollingStockType.FREIGHT_CAR
            gauge = RollingStockFreightCarSerializer.parse_gauge_from_name(name) if is_freight_car else None

            rolling_stock = RollingStock(
                gauge=gauge,
                is_sigo=True if sigo_number is not None else False,
                sigo_number=sigo_number,
                painted_identifier=name,
                regional=RollingStockSerializer.get_regional(name),
            )
            rolling_stock.save()

        if car_type == RollingStock.RollingStockType.LOCOMOTIVE:
            locomotive = RollingStockLocomotiveSerializer.create_from_name(name, rolling_stock)
        elif car_type == RollingStock.RollingStockType.FREIGHT_CAR:
            freight_car = RollingStockFreightCarSerializer.create_from_name(name, rolling_stock)

        return rolling_stock

    def to_representation(self, instance: RollingStock):
        instance_dict = super(RollingStockSerializer, self).to_representation(instance)
        instance_dict['metadata'] = self.read_metadata(instance)
        return instance_dict
