from django.contrib import admin
from django.db import models

from api.models.generic_audited_model import GenericAuditedModel
from api.models.rolling_stock_model import RollingStock
from api.models.passenger_car_material_model import PassengerCarMaterial
from api.models.passenger_car_type_model import PassengerCarType


class PassengerCar(GenericAuditedModel):

    rolling_stock = models.OneToOneField(to=RollingStock, on_delete=models.CASCADE, null=False)
    material = models.ForeignKey(to=PassengerCarMaterial, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(to=PassengerCarType, on_delete=models.SET_NULL, null=True)


class PassengerCarAdmin(admin.ModelAdmin):
    pass


admin.site.register(PassengerCar, PassengerCarAdmin)
