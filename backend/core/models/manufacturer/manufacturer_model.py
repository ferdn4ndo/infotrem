from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel


class Manufacturer(GenericAuditedModel):

    short_name = models.CharField(max_length=20, verbose_name=_("Short name of the manufacturer"))
    full_name = models.CharField(max_length=255, verbose_name=_("Long (full) name of the manufacturer"))


class ManufacturerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Manufacturer, ManufacturerAdmin)
