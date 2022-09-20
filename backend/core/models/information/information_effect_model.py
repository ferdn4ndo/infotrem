from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.information.information_model import Information


class InformationEffect(GenericAuditedModel):
    information = models.ForeignKey(
        to=Information,
        related_name='effects',
        on_delete=models.CASCADE,
        verbose_name=_("Information object where the changes will take effect once accepted"),
    )
    field_name = models.TextField(
        max_length=255,
        verbose_name=_("Name of the field that will have the information changed once accepted"),
    )
    old_value = models.TextField(
        max_length=1024,
        null=True,
        verbose_name=_("The original value of the field (before the information is accepted)"),
    )
    new_value = models.TextField(
        max_length=1024,
        null=True,
        verbose_name=_("The new value of the field (after the information is accepted)"),
    )


class InformationEffectAdmin(admin.ModelAdmin):
    pass


admin.site.register(InformationEffect, InformationEffectAdmin)
