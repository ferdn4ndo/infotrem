from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.company.company_model import Company
from core.models.generic_audited_model import GenericAuditedModel


class Route(GenericAuditedModel):

    name = models.CharField(max_length=255, verbose_name=_("Name of the route"))
    builder_railroad = models.ForeignKey(to=Company, on_delete=models.SET_NULL, null=True)


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Route, RouteAdmin)
