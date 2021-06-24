from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel


class Path(GenericAuditedModel):

    class PathStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', _("Path is active (with traffic)")
        INACTIVE = 'INACTIVE', _("Path is inactive (exists but without traffic)")
        ERADICATED = 'ERADICATED', _("Path was already eradicated")

    name = models.CharField(max_length=255, verbose_name=_("Name of the section path"))
    status = models.CharField(max_length=100, choices=PathStatus.choices, null=True)


class PathAdmin(admin.ModelAdmin):
    pass


admin.site.register(Path, PathAdmin)
