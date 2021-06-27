from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_audited_model import GenericAuditedModel


class Company(GenericAuditedModel):

    abbrev = models.TextField(max_length=20, verbose_name=_("Abbreviation (short name) of the company"))
    name = models.TextField(max_length=255, verbose_name=_("Name of the company"))


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
