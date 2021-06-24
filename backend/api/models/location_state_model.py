from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel


class LocationState(GenericAuditedModel):
    abbrev = models.CharField(max_length=2, verbose_name=_("Abbreviation of the state with 2 letters"))
    name = models.CharField(max_length=255, verbose_name=_("Full name of the state"))
    ibge_id = models.PositiveIntegerField(null=True, verbose_name=_("IBGE ID of the state"))


class LocationStateAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocationState, LocationStateAdmin)
