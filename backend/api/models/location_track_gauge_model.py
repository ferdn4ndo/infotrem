from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.location_model import Location
from api.models.track_gauge_model import TrackGauge


class LocationTrackGauge(GenericAuditedModel):

    location = models.ForeignKey(
        to=Location,
        related_name='location_information',
        on_delete=models.CASCADE,
        verbose_name=_("Location which has the track gauge"),
    )
    track_gauge = models.ForeignKey(
        to=TrackGauge,
        on_delete=models.PROTECT,
        verbose_name=_("Track gauge associated with the location"),
    )


class LocationTrackGaugeAdmin(admin.ModelAdmin):
    pass


admin.site.register(LocationTrackGauge, LocationTrackGaugeAdmin)
