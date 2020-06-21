import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField

from infotrem.models.information import Information


class TrackGaugeConfiguration(models.Model):

    class Meta:
        app_label = 'infotrem'

    gauge_configuration_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.CharField(max_length=32, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    gauges = JSONField(verbose_name="Array with the gauges of current configuration")


class Location(models.Model):

    class LocationType(models.TextChoices):
        STATION = 'STATION', _("Station")
        CROSSING_YARD = 'CROSSING_YARD', _("Crossing Yard")
        CLASSIFICATION_YARD = 'CLASSIFICATION_YARD', _("Classification Yard")
        TUNNEL = 'TUNNEL', _("Tunnel")
        BRIDGE = 'BRIDGE', _("Bridge")
        OTHERS = 'OTHERS', _("Other Type")

    class Meta:
        app_label = 'infotrem'

    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    abbrev = models.TextField(max_length=10, db_index=True)
    name = models.TextField(max_length=255)
    type = models.CharField(max_length=100, choices=LocationType.choices)
    track_gauge = models.ForeignKey(to=TrackGaugeConfiguration, on_delete=models.PROTECT)
    center_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    center_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=datetime.utcnow, editable=False)
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="editor+")
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)


class LocationTrackGauge(models.Model):
    class Meta:
        app_label = 'infotrem'

    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class LocationInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)
