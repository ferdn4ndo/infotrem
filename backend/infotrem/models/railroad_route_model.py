import uuid

from django.db import models

from infotrem.models.information_model import Information
from infotrem.models.location_model import Location
from infotrem.models.railroad_company_model import RailroadCompany


class RailroadRoute(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    builder_railroad = models.ForeignKey(to=RailroadCompany, on_delete=models.SET_NULL, null=True)


class RailroadRouteInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad_route = models.ForeignKey(to=RailroadRoute, related_name='route_information', on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RailroadRouteSection(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad_route = models.ForeignKey(to=RailroadRoute, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    builder_railroad = models.ForeignKey(to=RailroadCompany, on_delete=models.SET_NULL, null=True)
    build_year = models.PositiveIntegerField(null=True)


class RailroadRouteSectionInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad_route_section = models.ForeignKey(to=RailroadRoute, on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RailroadRouteSectionLocation(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad_route = models.ForeignKey(to=RailroadRoute, related_name='route_locations', on_delete=models.CASCADE)
    railroad_route_section = models.ForeignKey(to=RailroadRouteSection, related_name='section_locations', on_delete=models.CASCADE)
    location = models.ForeignKey(to=Location, related_name='route_sections', on_delete=models.CASCADE)
    location_route_order = models.IntegerField(verbose_name="Ordering number inside the route, from origin to destiny")

    def save(self, *args, **kwargs):
        if self.location_route_order is None:
            self.location_route_order = RailroadRouteSectionLocation.objects.filter(
                railroad_route=self.railroad_route,
            ).order_by('-location_route_order').first().location_route_order + 1
        super().save(*args, **kwargs)


class RailroadRouteSectionLocationKilometer(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad_route_section_location = models.ForeignKey(to=RailroadRouteSectionLocation, related_name='kilometers', on_delete=models.CASCADE)
    kilometer = models.FloatField(verbose_name="Kilometer of the location inside the route")
    kilometer_year = models.PositiveIntegerField(null=True, verbose_name="Year of the recorded kilometer")
    elevation = models.FloatField(null=True, verbose_name="Elevation (in meters) of the location kilometer")


class RailroadRouteSectionPath(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad_route = models.ForeignKey(to=RailroadRoute, on_delete=models.CASCADE)
    railroad_route_section = models.ForeignKey(to=RailroadRouteSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class RailroadRouteSectionPathPoint(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad_route_section_path = models.ForeignKey(to=RailroadRouteSectionPath, related_name='points', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    elevation = models.FloatField(null=True, verbose_name="Elevation (in meters) of the location")
