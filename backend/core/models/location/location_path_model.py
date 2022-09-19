from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.location.location_model import Location
from core.models.path.path_model import Path


class LocationPath(GenericAuditedModel):

    location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE,
        verbose_name=_("The location which has the path")
    )
    path = models.ForeignKey(
        to=Path,
        on_delete=models.CASCADE,
        verbose_name=_("The path associated with the location")
    )


class LocationPathAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocationPath, LocationPathAdmin)
