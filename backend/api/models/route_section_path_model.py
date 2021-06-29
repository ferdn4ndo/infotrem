from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .path_model import Path
from .route_section_model import RouteSection


class RouteSectionPath(GenericAuditedModel):

    railroad_route_section = models.ForeignKey(
        to=RouteSection,
        on_delete=models.CASCADE,
        verbose_name=_("The route section which has the path")
    )
    path = models.ForeignKey(
        to=Path,
        on_delete=models.CASCADE,
        verbose_name=_("The path associated with the route section")
    )


class RouteSectionPathAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteSectionPath, RouteSectionPathAdmin)
