from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.information.information_model import Information
from core.models.manufacturer.manufacturer_model import Manufacturer


class ManufacturerInformation(GenericAuditedModel):

    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        verbose_name=_("Manufacturer which holds the information"),
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name=_("Information associated with the manufacturer"),
    )


class ManufacturerInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(ManufacturerInformation, ManufacturerInformationAdmin)