from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.path_model import Path


class PathPoint(GenericAuditedModel):

    path = models.ForeignKey(
        to=Path,
        related_name='points',
        on_delete=models.CASCADE,
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    elevation = models.FloatField(null=True, verbose_name=_("Elevation (in meters) of the point"))


class PathPointAdmin(admin.ModelAdmin):
    pass


admin.site.register(PathPoint, PathPointAdmin)
