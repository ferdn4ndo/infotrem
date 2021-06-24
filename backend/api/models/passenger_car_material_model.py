from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.generic_model import GenericModel


class PassengerCarMaterial(GenericModel):

    letter = models.CharField(max_length=1, unique=True, db_index=True, blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name=_("Name of the material of the passenger cars"))


class PassengerCarMaterialAdmin(admin.ModelAdmin):
    pass


admin.site.register(PassengerCarMaterial, PassengerCarMaterialAdmin)
