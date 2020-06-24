import uuid

from django.db import models

from infotrem.models.rolling_stock import RollingStock


class RollingStockPassengerCarType(models.Model):

    class Meta:
        app_label = 'infotrem'

    letter = models.CharField(max_length=1, primary_key=True, unique=True, db_index=True, blank=False, null=False)
    name = models.CharField(max_length=100)


class RollingStockPassengerCarMaterial(models.Model):

    class Meta:
        app_label = 'infotrem'

    letter = models.CharField(max_length=1, primary_key=True, unique=True, db_index=True, blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name="Name of the material of passenger cars")


class RollingStockPassengerCar(models.Model):

    class Meta:
        app_label = 'infotrem'

    rolling_stock = models.OneToOneField(to=RollingStock, on_delete=models.CASCADE, primary_key=True)
    material = models.ForeignKey(to=RollingStockPassengerCarMaterial, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(to=RollingStockPassengerCarType, on_delete=models.SET_NULL, null=True)


