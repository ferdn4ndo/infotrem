import uuid

from django.db import models

from infotrem.models.rolling_stock import RollingStock
from infotrem.models.track_gauge import TrackGauge


class RollingStockFreightCarCategory(models.Model):

    class Meta:
        app_label = 'infotrem'

    letter = models.CharField(max_length=1, primary_key=True, unique=True, db_index=True, blank=False, null=False)
    name = models.CharField(max_length=100)


class RollingStockFreightCarGrossWeightType(models.Model):

    class Meta:
        app_label = 'infotrem'

    letter = models.CharField(max_length=1, primary_key=True, unique=True, db_index=True, blank=False, null=False)
    max_gross_tons = models.FloatField(verbose_name="Max gross weight of the type")
    gauge = models.ForeignKey(to=TrackGauge, on_delete=models.PROTECT)


class RollingStockFreightCarType(models.Model):

    class Meta:
        app_label = 'infotrem'

    letters = models.CharField(max_length=2, primary_key=True, unique=True, db_index=True, blank=False, null=False)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(to=RollingStockFreightCarCategory, on_delete=models.PROTECT)


class RollingStockFreightCar(models.Model):

    class Meta:
        app_label = 'infotrem'

    rolling_stock = models.OneToOneField(to=RollingStock, on_delete=models.CASCADE, primary_key=True)
    model_type = models.ForeignKey(to=RollingStockFreightCarType, on_delete=models.SET_NULL, null=True)
    gross_weight_type = models.ForeignKey(to=RollingStockFreightCarGrossWeightType, on_delete=models.SET_NULL, null=True)
