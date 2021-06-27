from django.contrib import admin
from django.db import models

from .generic_audited_model import GenericAuditedModel
from .information_model import Information
from .route_model import Route


class RouteSectionInformation(GenericAuditedModel):

    railroad_route_section = models.ForeignKey(to=Route, on_delete=models.PROTECT)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RouteSectionInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteSectionInformation, RouteSectionInformationAdmin)
