from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .company_model import Company


class Route(GenericAuditedModel):

    name = models.CharField(max_length=255, verbose_name=_("Name of the route"))
    builder_railroad = models.ForeignKey(to=Company, on_delete=models.SET_NULL, null=True)


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Route, RouteAdmin)
