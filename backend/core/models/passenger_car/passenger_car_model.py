from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.passenger_car.passenger_car_material_model import PassengerCarMaterial
from core.models.passenger_car.passenger_car_type_model import PassengerCarType
from core.models.rolling_stock.rolling_stock_model import RollingStock


class PassengerCar(GenericAuditedModel):

    rolling_stock = models.OneToOneField(
        to=RollingStock,
        on_delete=models.CASCADE,
        null=False,
        verbose_name=_("Rolling stock that is a passenger car")
    )
    material = models.ForeignKey(
        to=PassengerCarMaterial,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Material of the passenger car")
    )
    type = models.ForeignKey(
        to=PassengerCarType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Type of the passenger car")
    )


class PassengerCarAdmin(admin.ModelAdmin):
    pass


admin.site.register(PassengerCar, PassengerCarAdmin)
