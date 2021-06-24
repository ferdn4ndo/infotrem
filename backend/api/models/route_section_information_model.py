from django.contrib import admin
from django.db import models

from api.models.generic_audited_model import GenericAuditedModel
from api.models.information_model import Information
from api.models.route_model import Route


class RouteSectionInformation(GenericAuditedModel):

    railroad_route_section = models.ForeignKey(to=Route, on_delete=models.PROTECT)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RouteSectionInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteSectionInformation, RouteSectionInformationAdmin)
