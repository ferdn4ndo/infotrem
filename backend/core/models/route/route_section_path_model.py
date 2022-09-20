from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.path.path_model import Path
from core.models.route.route.route_section_path_view import RouteSectionPathAdmin
from core.models.route.route_section_model import RouteSection


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


admin.site.register(RouteSectionPath, RouteSectionPathAdmin)
