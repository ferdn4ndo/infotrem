from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.generic_model import GenericModel
from api.models.company_model import Company


class SigoRegional(GenericModel):

    letter = models.CharField(max_length=1, primary_key=True)
    original_company = models.ForeignKey(to=Company, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, verbose_name=_("Nome da regional"))
    abbrev = models.CharField(max_length=20, null=True, verbose_name=_("Sigla da regional"))


class SigoRegionalAdmin(admin.ModelAdmin):
    pass


admin.site.register(SigoRegional, SigoRegionalAdmin)
