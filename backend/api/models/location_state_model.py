from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_model import GenericModel


class LocationState(GenericModel):
    abbrev = models.CharField(max_length=2, verbose_name=_("Abbreviation of the state with 2 letters"))
    name = models.CharField(max_length=255, verbose_name=_("Full name of the state"))
    ibge_id = models.PositiveIntegerField(null=True, verbose_name=_("IBGE ID of the state"))


class LocationStateAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocationState, LocationStateAdmin)
