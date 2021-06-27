from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .information_model import Information
from .company_model import Company


class CompanyInformation(GenericAuditedModel):

    railroad = models.ForeignKey(
        to=Company,
        related_name='company_information',
        on_delete=models.CASCADE,
        verbose_name=_("Company which holds the information"),
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name=_("Information associated with the company"),
    )


class CompanyInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(CompanyInformation, CompanyInformationAdmin)
