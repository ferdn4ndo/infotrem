from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.manufacturer.manufacturer_model import Manufacturer
from core.models.rolling_stock.rolling_stock_model import RollingStock
from core.models.track_gauge.track_gauge_model import TrackGauge


class LocomotiveDesign(GenericAuditedModel):

    name = models.CharField(max_length=100, unique=True)
    gauge = models.ForeignKey(to=TrackGauge, on_delete=models.PROTECT, null=True)
    prime_mover = models.CharField(max_length=100, choices=RollingStock.RollingStockPrimeMover.choices, null=True)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        related_name='locomotive_design_manufacturer',
        on_delete=models.SET_NULL,
        null=True
    )
    first_unit_year = models.IntegerField(null=True, verbose_name=_("Year when the first unit was produced"))
    adhesion_factor = models.FloatField(null=True, verbose_name=_("Adhesion factor of the locomotive (0 to 1)"))
    allow_multiple_units = models.BooleanField(null=True, verbose_name=_("If allows multiple traction units connected"))
    brake_system = models.CharField(max_length=200, null=True, verbose_name=_("Brake System (eg. 26L)"))
    cooling_fluid_capacity = models.FloatField(null=True, verbose_name=_("Capacity (in liters) of the cooling fluid"))
    cylinders_size = models.CharField(max_length=200, null=True, verbose_name=_("Cylinders Size"))
    fuel_capacity = models.CharField(max_length=200, null=True, verbose_name=_("Range of size of the fuel tank"))
    generator = models.CharField(max_length=200, null=True, verbose_name=_("Generator (eg. D32T)"))
    height = models.FloatField(null=True, verbose_name=_("Height of the locomotive in meters"))
    horsepower_available = models.PositiveIntegerField(null=True, verbose_name=_("Traction (available) horsepower"))
    horsepower_total = models.PositiveIntegerField(null=True, verbose_name=_("Total horsepower"))
    length = models.FloatField(null=True, verbose_name=_("Length of the locomotive in meters"))
    lubricant_oil_capacity = models.FloatField(null=True, verbose_name=_("Capacity (in liters) of the lubricant oil"))
    minimum_track_radius = models.FloatField(null=True, verbose_name=_("Minimum track curve radius in meters"))
    motor_builder = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.SET_NULL,
        related_name='locomotive_design_motor_builder',
        null=True,
        verbose_name=_("The manufacturer of the locomotive's motor")
    )
    motor_capacity = models.CharField(max_length=200, null=True, verbose_name=_("Motor Capacity"))
    motor_type = models.CharField(max_length=200, null=True, verbose_name=_("Motor Type"))
    nickname = models.CharField(max_length=200, null=True, verbose_name=_("Nickname of the model"))
    primary_motor = models.CharField(max_length=200, null=True, verbose_name=_("Primary motor (eg: 12-645E)"))
    rpm_limit = models.IntegerField(null=True, verbose_name=_("RMP limit of the motor"))
    sand_capacity = models.FloatField(null=True, verbose_name=_("Total sand capacity in cubic meters"))
    serial_number_range = models.CharField(max_length=200, null=True, verbose_name=_("Serial number range"))
    traction_effort = models.FloatField(null=True, verbose_name=_("Traction effort in kgf"))
    traction_motor = models.CharField(max_length=200, null=True, verbose_name=_("Traction motor (eg: D29)"))
    truck_type = models.CharField(max_length=200, null=True, verbose_name=_("Truck type"))
    velocity_max = models.FloatField(
        null=True,
        verbose_name=_("Maximum operational velocity of the locomotive in km/h"),
    )
    velocity_min = models.FloatField(
        null=True,
        verbose_name=_("Minimum operational velocity of the locomotive in km/h"),
    )
    weight = models.FloatField(null=True, verbose_name=_("Weight of the locomotive in kilograms"))
    weight_adherent = models.FloatField(null=True, verbose_name=_("Adherent weight of the locomotive in kilograms"))
    weight_per_axle = models.FloatField(null=True, verbose_name=_("Weight per axle of the locomotive in kilograms"))
    wheel_arrangement_aar = models.CharField(max_length=20, null=True, verbose_name=_("AAR wheelset, eg: A1A-A1A"))
    wheel_arrangement_whyte = models.CharField(max_length=20, null=True, verbose_name=_("Whyte wheelset, eg: 0-4-2"))
    wheel_diameter = models.FloatField(null=True, verbose_name=_("Wheel diameter in millimeters"))
    wheelbase = models.FloatField(null=True, verbose_name=_("Wheelbase in meters"))
    width = models.FloatField(null=True, verbose_name=_("Width of the locomotive in meters"))
    wikipedia_url = models.CharField(max_length=255, null=True, verbose_name=_("Wikipedia URL of the model"))


class LocomotiveDesignAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocomotiveDesign, LocomotiveDesignAdmin)
