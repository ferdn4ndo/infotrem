from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .company_model import Company
from .route_model import Route


class RouteSection(GenericAuditedModel):

    railroad_route = models.ForeignKey(to=Route, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    builder_railroad = models.ForeignKey(to=Company, on_delete=models.SET_NULL, null=True)
    build_year = models.PositiveIntegerField(null=True, verbose_name=_("Year when the route section was built"))


class RouteSectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteSection, RouteSectionAdmin)
