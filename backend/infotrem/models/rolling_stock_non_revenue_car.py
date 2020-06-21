from django.db import models
from django.utils.translation import ugettext_lazy as _

from infotrem.models.rolling_stock import RollingStock


class RollingStockNonRevenueCarType(models.Model):

    class Meta:
        app_label = 'infotrem'

    class RollingStockNonRevenueCarCategory(models.TextChoices):
        ELECTRICAL_MAINTENANCE = 'ELECTRICAL_MAINTENANCE', _('Equipment for Electrical Maintenance')
        RESCUE = 'RESCUE', _('Rescue Equipment')
        TRACK = 'TRACK', _('Track Equipment')
        VEGETATION = 'VEGETATION', _('Vegetation Equipment')
        OTHER = 'OTHER', _('Other Equipment')

    letters = models.CharField(max_length=2, primary_key=True, unique=True, db_index=True, blank=False, null=False)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=RollingStockNonRevenueCarCategory.choices, null=True)


class RollingStockNonRevenueCar(models.Model):

    class Meta:
        app_label = 'infotrem'

    rolling_stock = models.OneToOneField(to=RollingStock, on_delete=models.CASCADE, primary_key=True)
    type = models.ForeignKey(to=RollingStockNonRevenueCarType, on_delete=models.SET_NULL, null=True)
    is_self_propelled = models.BooleanField(default=False, verbose_name="If the car is self propelled")
    prime_mover = models.CharField(max_length=100, choices=RollingStock.RollingStockPrimeMover.choices, null=True)
