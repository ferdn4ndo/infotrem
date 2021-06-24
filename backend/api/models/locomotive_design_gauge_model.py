from django.contrib import admin
from django.db import models

from api.models.generic_audited_model import GenericAuditedModel
from api.models.locomotive_design_model import LocomotiveDesign
from api.models.track_gauge_model import TrackGauge


class LocomotiveDesignGauge(GenericAuditedModel):

    locomotive_design = models.ForeignKey(to=LocomotiveDesign, on_delete=models.CASCADE, null=True)
    gauge = models.ForeignKey(to=TrackGauge, on_delete=models.PROTECT, null=True)


class LocomotiveDesignGaugeAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocomotiveDesignGauge, LocomotiveDesignGaugeAdmin)