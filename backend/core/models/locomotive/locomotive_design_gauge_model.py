from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.locomotive.locomotive_design_model import LocomotiveDesign
from core.models.track_gauge.track_gauge_model import TrackGauge


class LocomotiveDesignGauge(GenericAuditedModel):

    locomotive_design = models.ForeignKey(
        to=LocomotiveDesign,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("Locomotive design that uses the gauge")
    )
    gauge = models.ForeignKey(
        to=TrackGauge,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_("Gauge associated with the locomotive design")
    )


class LocomotiveDesignGaugeAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocomotiveDesignGauge, LocomotiveDesignGaugeAdmin)
