from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.company.company_model import Company
from core.models.generic_audited_model import GenericAuditedModel
from core.models.information.information_model import Information


class CompanyInformation(GenericAuditedModel):

    company = models.ForeignKey(
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
