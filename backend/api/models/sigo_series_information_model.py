from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .information_model import Information


class SigoSeriesInformation(GenericAuditedModel):

    sigo_start_number = models.IntegerField(
        blank=False,
        null=False,
        verbose_name=_("SIGO range start number"),
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(0)
        ]
    )
    sigo_end_number = models.IntegerField(
        blank=False,
        null=False,
        verbose_name=_("SIGO range end number"),
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(0)
        ]
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name=_("The information about the numeric range"),
    )


class SigoSeriesInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(SigoSeriesInformation, SigoSeriesInformationAdmin)
