from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .location_model import Location
from .route_model import Route
from .route_section_model import RouteSection


class RouteSectionLocation(GenericAuditedModel):

    railroad_route = models.ForeignKey(to=Route, related_name='route_locations', on_delete=models.CASCADE)
    railroad_route_section = models.ForeignKey(
        to=RouteSection,
        related_name='section_locations',
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(to=Location, related_name='route_sections', on_delete=models.CASCADE)
    location_route_order = models.IntegerField(
        verbose_name=_("Ordering number inside the route, from origin to destiny"),
    )

    def save(self, *args, **kwargs):
        if self.location_route_order is None:
            self.location_route_order = RouteSectionLocation.objects.filter(
                railroad_route=self.railroad_route,
            ).order_by('-location_route_order').first().location_route_order + 1
        super().save(*args, **kwargs)


class RouteSectionLocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteSectionLocation, RouteSectionLocationAdmin)
