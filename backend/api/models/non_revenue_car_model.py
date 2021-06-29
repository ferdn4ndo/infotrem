from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .rolling_stock_model import RollingStock
from .non_revenue_car_type_model import NonRevenueCarType


class NonRevenueCar(GenericAuditedModel):

    rolling_stock = models.OneToOneField(to=RollingStock, on_delete=models.CASCADE, null=False)
    type = models.ForeignKey(to=NonRevenueCarType, on_delete=models.SET_NULL, null=True)
    is_self_propelled = models.BooleanField(default=False, verbose_name=_("If the car is self propelled"))
    prime_mover = models.CharField(max_length=100, choices=RollingStock.RollingStockPrimeMover.choices, null=True)


class NonRevenueCarAdmin(admin.ModelAdmin):
    pass


admin.site.register(NonRevenueCar, NonRevenueCarAdmin)
