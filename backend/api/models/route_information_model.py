from django.contrib import admin
from django.db import models

from .generic_audited_model import GenericAuditedModel
from .information_model import Information
from .route_model import Route


class RouteInformation(GenericAuditedModel):

    railroad_route = models.ForeignKey(to=Route, related_name='route_information', on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RouteInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RouteInformation, RouteInformationAdmin)
