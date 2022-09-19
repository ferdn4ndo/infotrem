from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.route.route_section_location_model import RouteSectionLocation


class RouteSectionLocationKilometer(GenericAuditedModel):

    railroad_route_section_location = models.ForeignKey(
        to=RouteSectionLocation,
        related_name='kilometers',
        on_delete=models.CASCADE
    )
    kilometer = models.FloatField(verbose_name=_("Kilometer of the location inside the route"))
    kilometer_year = models.PositiveIntegerField(null=True, verbose_name=_("Year of the recorded kilometer"))
    elevation = models.FloatField(null=True, verbose_name=_("Elevation (in meters) of the location kilometer"))


class RouteSectionLocationKilometerAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteSectionLocationKilometer, RouteSectionLocationKilometerAdmin)
