from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.information_model import Information
from api.models.manufacturer_model import Manufacturer


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
