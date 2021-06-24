from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel


class TrackGauge(GenericAuditedModel):
    code = models.CharField(max_length=32, unique=True, db_index=True)
    size = models.IntegerField(verbose_name=_("Gauge size in millimeters"))


class TrackGaugeAdmin(admin.ModelAdmin):
    pass


admin.site.register(TrackGauge, TrackGaugeAdmin)
