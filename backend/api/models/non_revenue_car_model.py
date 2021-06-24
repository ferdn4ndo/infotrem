from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.rolling_stock_model import RollingStock
from api.models.non_revenue_car_type_model import NonRevenueCarType


class NonRevenueCar(GenericAuditedModel):

    rolling_stock = models.OneToOneField(to=RollingStock, on_delete=models.CASCADE, null=False)
    type = models.ForeignKey(to=NonRevenueCarType, on_delete=models.SET_NULL, null=True)
    is_self_propelled = models.BooleanField(default=False, verbose_name=_("If the car is self propelled"))
    prime_mover = models.CharField(max_length=100, choices=RollingStock.RollingStockPrimeMover.choices, null=True)


class NonRevenueCarAdmin(admin.ModelAdmin):
    pass


admin.site.register(NonRevenueCar, NonRevenueCarAdmin)
