import re
from typing import Optional

from rest_framework import serializers

from core.models.locomotive.locomotive_design_model import LocomotiveDesign
from core.models.locomotive.locomotive_model import Locomotive
from core.models.rolling_stock.rolling_stock_model import RollingStock


class RollingStockLocomotiveModelSerializer(serializers.ModelSerializer):
    """Serializer for the LocomotiveDesign model"""

    class Meta:
        model = LocomotiveDesign
        excludes = ['rolling_stock']


class RollingStockLocomotiveSerializer(serializers.ModelSerializer):
    """Serializer for the Locomotive model"""
    model = RollingStockLocomotiveModelSerializer()

    class Meta:
        model = Locomotive
        excludes = ['rolling_stock']

    @staticmethod
    def parse_model_from_name(name: str) -> Optional[LocomotiveDesign]:
        name = name.upper().replace(" ", "_").replace("-", "_")
        parts = re.sub("_+", "_", name).split("_")
        for part in parts:
            models = LocomotiveDesign.objects.filter(name=part)
            if len(models) > 0:
                return models[0]

        return None

    @staticmethod
    def create_from_name(name: str, rolling_stock: RollingStock) -> Optional[Locomotive]:
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

        rolling_stock_loco = Locomotive.objects.get_or_create(
            rolling_stock=rolling_stock,
            model=model,
        )[0]

        rolling_stock_loco.adhesion_factor = model.adhesion_factor if model is not None else None
        rolling_stock_loco.allow_multiple_units = model.allow_multiple_units if model is not None else None
        rolling_stock_loco.brake_system = model.brake_system if model is not None else None
        rolling_stock_loco.cooling_fluid_capacity = model.cooling_fluid_capacity if model is not None else None
        rolling_stock_loco.cylinders_size = model.cylinders_size if model is not None else None
        rolling_stock_loco.build_year = None
        rolling_stock_loco.fuel_capacity = model.fuel_capacity if model is not None else None
        rolling_stock_loco.generator = model.generator if model is not None else None
        rolling_stock_loco.height = model.height if model is not None else None
        rolling_stock_loco.horsepower_available = model.horsepower_available if model is not None else None
        rolling_stock_loco.horsepower_total = model.horsepower_total if model is not None else None
        rolling_stock_loco.length = model.length if model is not None else None
        rolling_stock_loco.lubricant_oil_capacity = model.lubricant_oil_capacity if model is not None else None
        rolling_stock_loco.minimum_track_radius = model.minimum_track_radius if model is not None else None
        rolling_stock_loco.motor_builder = model.motor_builder if model is not None else None
        rolling_stock_loco.motor_capacity = model.motor_capacity if model is not None else None
        rolling_stock_loco.motor_type = model.motor_type if model is not None else None
        rolling_stock_loco.nickname = model.nickname if model is not None else None
        rolling_stock_loco.primary_motor = model.primary_motor if model is not None else None
        rolling_stock_loco.rpm_limit = model.rpm_limit if model is not None else None
        rolling_stock_loco.sand_capacity = model.sand_capacity if model is not None else None
        rolling_stock_loco.serial_number = None
        rolling_stock_loco.traction_effort = model.traction_effort if model is not None else None
        rolling_stock_loco.traction_motor = model.traction_motor if model is not None else None
        rolling_stock_loco.truck_type = model.truck_type if model is not None else None
        rolling_stock_loco.velocity_max = model.velocity_max if model is not None else None
        rolling_stock_loco.velocity_min = model.velocity_min if model is not None else None
        rolling_stock_loco.weight = model.weight if model is not None else None
        rolling_stock_loco.weight_adherent = model.weight_adherent if model is not None else None
        rolling_stock_loco.weight_per_axle = model.weight_per_axle if model is not None else None
        rolling_stock_loco.wheel_arrangement_aar = model.wheel_arrangement_aar if model is not None else None
        rolling_stock_loco.wheel_arrangement_whyte = model.wheel_arrangement_whyte if model is not None else None
        rolling_stock_loco.wheel_diameter = model.wheel_diameter if model is not None else None
        rolling_stock_loco.wheelbase = model.wheelbase if model is not None else None
        rolling_stock_loco.width = model.width if model is not None else None

        rolling_stock_loco.save()

        return rolling_stock_loco
