from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.company.company_model import Company
from core.models.generic_model import GenericModel


class SigoRegional(GenericModel):

    letter = models.CharField(max_length=1)
    original_company = models.ForeignKey(to=Company, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, verbose_name=_("Name of the regional"))
    abbrev = models.CharField(max_length=20, null=True, verbose_name=_("Abbreviation of the regional"))


class SigoRegionalAdmin(admin.ModelAdmin):
    pass


admin.site.register(SigoRegional, SigoRegionalAdmin)
