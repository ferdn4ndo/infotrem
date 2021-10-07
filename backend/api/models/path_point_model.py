from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .path_model import Path


class PathPoint(GenericAuditedModel):

    path = models.ForeignKey(
        to=Path,
        related_name='points',
        on_delete=models.CASCADE,
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    elevation = models.FloatField(null=True, verbose_name=_("Elevation (in meters) of the point"))
    order = models.FloatField(verbose_name=_("Value used to sort the points"))


class PathPointAdmin(admin.ModelAdmin):
    pass


admin.site.register(PathPoint, PathPointAdmin)
