from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.freight_car.freight_car_gross_weight_type_model import FreightCarGrossWeightType
from core.models.freight_car.freight_car_type_model import FreightCarType
from core.models.generic_audited_model import GenericAuditedModel
from core.models.rolling_stock.rolling_stock_model import RollingStock


class FreightCar(GenericAuditedModel):

    rolling_stock = models.OneToOneField(to=RollingStock, on_delete=models.CASCADE, null=False)
    model_type = models.ForeignKey(to=FreightCarType, on_delete=models.SET_NULL, null=True)
    gross_weight_type = models.ForeignKey(
        to=FreightCarGrossWeightType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Gross weight type (represented as a letter) of the freight car")
    )


class FreightCarAdmin(admin.ModelAdmin):
    pass


admin.site.register(FreightCar, FreightCarAdmin)
