from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.information_model import Information
from api.models.company_paint_scheme_model import CompanyPaintScheme


class CompanyPaintSchemeInformation(GenericAuditedModel):

    paint_scheme = models.ForeignKey(
        to=CompanyPaintScheme,
        related_name='railroad_information',
        on_delete=models.CASCADE,
        verbose_name=_("Paint scheme which holds the information")
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name=_("Information associated with the paint scheme"),
    )


class CompanyPaintSchemeInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(CompanyPaintSchemeInformation, CompanyPaintSchemeInformationAdmin)