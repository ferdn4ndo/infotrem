from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .information_model import Information
from .route_model import Route


class RouteInformation(GenericAuditedModel):

    railroad_route = models.ForeignKey(
        to=Route,
        related_name='route_information',
        on_delete=models.CASCADE,
        verbose_name=_("Route that holds the information"),
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name=_("Information associated with the route"),
    )


class RouteInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteInformation, RouteInformationAdmin)
