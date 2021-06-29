from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_model import GenericModel
from .location_state_model import LocationState


class LocationCity(GenericModel):
    state = models.ForeignKey(
        to=LocationState,
        on_delete=models.CASCADE,
        verbose_name=_("State where the city is situated")
    )
    name = models.CharField(max_length=255, verbose_name=_("Name of the city"))
    ibge_id = models.PositiveIntegerField(null=True, verbose_name=_("IBGE ID of the city"))


class LocationCityAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocationCity, LocationCityAdmin)
