import uuid

from django.db import models

from infotrem.models.manufacturer_model import Manufacturer
from infotrem.models.rolling_stock import RollingStock
from infotrem.models.track_gauge_model import TrackGauge


class RollingStockLocomotiveModel(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    gauge = models.ForeignKey(to=TrackGauge, on_delete=models.PROTECT, null=True)
    prime_mover = models.CharField(max_length=100, choices=RollingStock.RollingStockPrimeMover.choices, null=True)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.SET_NULL, null=True)
    first_unit_year = models.IntegerField(null=True, verbose_name="Year when the first unit was produced")
    adhesion_factor = models.FloatField(null=True, verbose_name="Adhesion factor of the locomotive (0 to 1)")
    allow_multiple_units = models.BooleanField(null=True, verbose_name="If allows multiple traction units connected")
    brake_system = models.CharField(max_length=200, null=True, verbose_name="Brake System (eg. 26L)")
    cooling_fluid_capacity = models.FloatField(null=True, verbose_name="Capacity (in liters) of the cooling fluid")
    cylinders_size = models.CharField(max_length=200, null=True, verbose_name="Cylinders Size")
    fuel_capacity = models.CharField(max_length=200, null=True, verbose_name="Range of size of the fuel tank")
    generator = models.CharField(max_length=200, null=True, verbose_name="Generator (eg. D32T)")
    height = models.FloatField(null=True, verbose_name="Height of the locomotive in meters")
    horsepower_available = models.PositiveIntegerField(null=True, verbose_name="Traction (available) horsepower")
    horsepower_total = models.PositiveIntegerField(null=True, verbose_name="Total horsepower")
    length = models.FloatField(null=True, verbose_name="Length of the locomotive in meters")
    lubricant_oil_capacity = models.FloatField(null=True, verbose_name="Capacity (in liters) of the lubricant oil")
    minimum_track_radius = models.FloatField(null=True, verbose_name="Minimum track curve radius in meters")
    motor_builder = models.ForeignKey(to=Manufacturer, on_delete=models.SET_NULL, null=True)
    motor_capacity = models.CharField(max_length=200, null=True, verbose_name="Motor Capacity")
    motor_type = models.CharField(max_length=200, null=True, verbose_name="Motor Type")
    nickname = models.CharField(max_length=200, null=True, verbose_name="Nickname of the model")
    primary_motor = models.CharField(max_length=50, null=True, verbose_name="Primary motor (eg: 12-645E)")
    rpm_limit = models.IntegerField(null=True, verbose_name="RMP limit of the motor")
    sand_capacity = models.FloatField(null=True, verbose_name="Total sand capacity in cubic meters")
    serial_number_range = models.CharField(max_length=200, null=True, verbose_name="Serial number range")
    traction_effort = models.FloatField(null=True, verbose_name="Traction effort in kgf")
    traction_motor = models.CharField(max_length=50, null=True, verbose_name="Traction motor (eg: D29)")
    truck_type = models.CharField(max_length=200, null=True, verbose_name="Truck type")
    velocity_max = models.FloatField(null=True, verbose_name="Maximum operational velocity of the locomotive in km/h")
    velocity_min = models.FloatField(null=True, verbose_name="Minimum operational velocity of the locomotive in km/h")
    weight = models.FloatField(null=True, verbose_name="Weight of the locomotive in kilograms")
    weight_adherent = models.FloatField(null=True, verbose_name="Adherent weight of the locomotive in kilograms")
    weight_per_axle = models.FloatField(null=True, verbose_name="Weight per axle of the locomotive in kilograms")
    wheel_arrangement_aar = models.CharField(max_length=20, null=True, verbose_name="AAR wheelset, eg: A1A-A1A")
    wheel_arrangement_whyte = models.CharField(max_length=20, null=True, verbose_name="Whyte wheelset, eg: 0-4-2")
    wheel_diameter = models.FloatField(null=True, verbose_name="Wheel diameter in millimeters")
    wheelbase = models.FloatField(null=True, verbose_name="Wheelbase in meters")
    width = models.FloatField(null=True, verbose_name="Width of the locomotive in meters")
    wikipedia_url = models.CharField(max_length=255, null=True, verbose_name="Wikipedia URL of the model")


class RollingStockLocomotive(models.Model):

    class Meta:
        app_label = 'infotrem'

    rolling_stock = models.OneToOneField(to=RollingStock, on_delete=models.CASCADE, primary_key=True)
    model = models.ForeignKey(to=RollingStockLocomotiveModel, null=True, on_delete=models.SET_NULL)

    adhesion_factor = models.FloatField(null=True, verbose_name="Adhesion factor of the locomotive (0 to 1)")
    allow_multiple_units = models.BooleanField(null=True, verbose_name="If allows multiple traction units connected")
    brake_system = models.CharField(max_length=200, null=True, verbose_name="Brake System (eg. 26L)")
    cooling_fluid_capacity = models.FloatField(null=True, verbose_name="Capacity (in liters) of the cooling fluid")
    cylinders_size = models.CharField(max_length=200, null=True, verbose_name="Cylinders Size")
    build_year = models.IntegerField(null=True, verbose_name="Year when it was build")
    fuel_capacity = models.FloatField(null=True, verbose_name="Maximum amount of liters of the tank")
    generator = models.CharField(max_length=200, null=True, verbose_name="Generator (eg. D32T)")
    height = models.FloatField(null=True, verbose_name="Height of the locomotive in meters")
    horsepower_available = models.PositiveIntegerField(null=True, verbose_name="Traction (available) horsepower")
    horsepower_total = models.PositiveIntegerField(null=True, verbose_name="Total horsepower")
    length = models.FloatField(null=True, verbose_name="Length of the locomotive in meters")
    lubricant_oil_capacity = models.FloatField(null=True, verbose_name="Capacity (in liters) of the lubricant oil")
    minimum_track_radius = models.FloatField(null=True, verbose_name="Minimum track curve radius in meters")
    motor_builder = models.ForeignKey(to=Manufacturer, on_delete=models.SET_NULL, null=True)
    motor_capacity = models.CharField(max_length=200, null=True, verbose_name="Motor Capacity")
    motor_type = models.CharField(max_length=200, null=True, verbose_name="Motor Type")
    nickname = models.CharField(max_length=200, null=True, verbose_name="Nickname of the model")
    primary_motor = models.CharField(max_length=50, null=True, verbose_name="Primary motor (eg: 12-645E)")
    rpm_limit = models.IntegerField(null=True, verbose_name="RMP limit of the motor")
    sand_capacity = models.FloatField(null=True, verbose_name="Total sand capacity in cubic meters")
    serial_number = models.CharField(max_length=200, null=True, verbose_name="Serial number of the locomotive")
    traction_effort = models.FloatField(null=True, verbose_name="Traction effort in kgf")
    traction_motor = models.CharField(max_length=50, null=True, verbose_name="Traction motor (eg: D29)")
    truck_type = models.CharField(max_length=200, null=True, verbose_name="Truck type")
    velocity_max = models.FloatField(null=True, verbose_name="Maximum operational velocity of the locomotive in km/h")
    velocity_min = models.FloatField(null=True, verbose_name="Minimum operational velocity of the locomotive in km/h")
    weight = models.FloatField(null=True, verbose_name="Weight of the locomotive in kilograms")
    weight_adherent = models.FloatField(null=True, verbose_name="Adherent weight of the locomotive in kilograms")
    weight_per_axle = models.FloatField(null=True, verbose_name="Weight per axle of the locomotive in kilograms")
    wheel_arrangement_aar = models.CharField(max_length=20, null=True, verbose_name="AAR wheelset, eg: A1A-A1A")
    wheel_arrangement_whyte = models.CharField(max_length=20, null=True, verbose_name="Whyte wheelset, eg: 0-4-2")
    wheel_diameter = models.FloatField(null=True, verbose_name="Wheel diameter in millimeters")
    wheelbase = models.FloatField(null=True, verbose_name="Wheelbase in meters")
    width = models.FloatField(null=True, verbose_name="Width of the locomotive in meters")
