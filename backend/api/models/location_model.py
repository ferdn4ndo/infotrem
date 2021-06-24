from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.location_city_model import LocationCity
from api.models.location_state_model import LocationState


class Location(GenericAuditedModel):

    class LocationType(models.TextChoices):
        STATION = 'STATION', _("Station")
        STOP = 'STOP', _("Stop")
        TERMINAL = 'TERMINAL', _("Terminal")
        CROSSING_YARD = 'CROSSING_YARD', _("Crossing Yard")
        CLASSIFICATION_YARD = 'CLASSIFICATION_YARD', _("Classification Yard")
        TUNNEL = 'TUNNEL', _("Tunnel")
        BRIDGE = 'BRIDGE', _("Bridge")
        OTHERS = 'OTHERS', _("Other Type")

    class LocationStatus(models.TextChoices):
        PROJECT = 'PROJECT', _("Project")
        UNDER_CONSTRUCTION = 'UNDER_CONSTRUCTION', _("Under Construction")
        WORKING = 'WORKING', _("Working")
        ABANDONED = 'ABANDONED', _("Abandoned")
        DEMOLISHED = 'DEMOLISHED', _("Demolished")
        TRANSFORMED = 'TRANSFORMED', _("Transformed")

    abbrev = models.TextField(max_length=10, unique=False, db_index=True, null=True)
    name = models.TextField(max_length=255)
    type = models.CharField(max_length=100, choices=LocationType.choices, null=True)
    status = models.CharField(max_length=100, choices=LocationStatus.choices, null=True)
    center_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    center_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    elevation = models.FloatField(null=True, verbose_name=_("Elevation (in meters) of the location"))
    city = models.ForeignKey(to=LocationCity, null=True, on_delete=models.SET_NULL)
    build_year = models.IntegerField(null=True, verbose_name=_("Year when it was built"))
    other_names = models.TextField(max_length=255, null=True)
    is_verified = models.BooleanField(default=False, verbose_name=_("If the place is verified and it's correct"))


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
