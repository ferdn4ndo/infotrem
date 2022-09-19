from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.information.information_model import Information
from core.models.route.route_model import Route


class RouteSectionInformation(GenericAuditedModel):

    railroad_route_section = models.ForeignKey(
        to=Route,
        on_delete=models.PROTECT,
        verbose_name=_("Section which holds the information"),
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name=_("Information associated with the section"),
    )


class RouteSectionInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteSectionInformation, RouteSectionInformationAdmin)
