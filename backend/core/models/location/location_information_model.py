from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.information.information_model import Information
from core.models.location.location_model import Location


class LocationInformation(GenericAuditedModel):

    location = models.ForeignKey(
        to=Location,
        related_name='information',
        on_delete=models.CASCADE,
        verbose_name=_("Location which holds the information"),
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name=_("Information associated with the location"),
    )


class LocationInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocationInformation, LocationInformationAdmin)
