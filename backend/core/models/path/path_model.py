from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel


class Path(GenericAuditedModel):

    class PathStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', _("Path is active (with frequent or sporadic usage)")
        INACTIVE = 'INACTIVE', _("Path is inactive (exists but not used anymore)")
        ERADICATED = 'ERADICATED', _("Path was already eradicated")

    class PathType(models.TextChoices):
        RAIL = 'RAIL', _("The path is a rail section")
        TUNNEL = 'TUNNEL', _("The path is a tunnel section")
        BRIDGE = 'BRIDGE', _("The path is a bridge section")
        BUILDING = 'BUILDING', _("The path represents a build (polygon)")
        AREA = 'AREA', _("The path represents an area (polygon)")

    name = models.CharField(max_length=255, verbose_name=_("Name of the section path"))
    type = models.CharField(max_length=100, choices=PathType.choices)
    status = models.CharField(max_length=100, choices=PathStatus.choices, null=True)


class PathAdmin(admin.ModelAdmin):
    pass


admin.site.register(Path, PathAdmin)
