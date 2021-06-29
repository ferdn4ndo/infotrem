from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .company_model import Company


class CompanyPaintScheme(GenericAuditedModel):

    name = models.CharField(max_length=255)
    railroad = models.ForeignKey(to=Company, on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name=_("Approximate date when the paint scheme has started"), null=True)
    end_date = models.DateField(verbose_name=_("Approximate date when the paint scheme has ended"), null=True)


class CompanyPaintSchemeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CompanyPaintScheme, CompanyPaintSchemeAdmin)
