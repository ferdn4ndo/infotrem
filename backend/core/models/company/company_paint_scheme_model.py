from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.company.company_model import Company
from core.models.generic_audited_model import GenericAuditedModel


class CompanyPaintScheme(GenericAuditedModel):

    name = models.CharField(max_length=255)
    railroad = models.ForeignKey(to=Company, on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name=_("Approximate date when the paint scheme has started"), null=True)
    end_date = models.DateField(verbose_name=_("Approximate date when the paint scheme has ended"), null=True)


class CompanyPaintSchemeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CompanyPaintScheme, CompanyPaintSchemeAdmin)
