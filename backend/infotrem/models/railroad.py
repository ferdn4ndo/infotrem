import uuid

from django.db import models

from infotrem.models.information import Information
from infotrem.models.location import Location


class RailroadCompany(models.Model):

    class Meta:
        app_label = 'infotrem'

    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    abbrev = models.TextField(max_length=10)
    name = models.TextField(max_length=255)


class RailroadCompanyInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    location = models.ForeignKey(to=RailroadCompany, on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RailroadPaintScheme(models.Model):

    class Meta:
        app_label = 'infotrem'

    paint_scheme_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    railroad = models.ForeignKey(to=RailroadCompany, on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name="Approx. date when the paint scheme has started", null=True)
    end_date = models.DateField(verbose_name="Approx. date when the paint scheme has ended", null=True)


class RailroadPaintSchemeInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    location = models.ForeignKey(to=RailroadPaintScheme, on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RailroadRoute(models.Model):

    class Meta:
        app_label = 'infotrem'

    route_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    builder_railroad = models.ForeignKey(to=RailroadCompany, on_delete=models.SET_NULL, null=True)


class RailroadRouteInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    location = models.ForeignKey(to=RailroadRoute, on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RailroadRouteLocation(models.Model):

    class Meta:
        app_label = 'infotrem'

    route_location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad_route = models.ForeignKey(to=RailroadRoute, on_delete=models.CASCADE)
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    location_route_order = models.IntegerField(verbose_name="Ordering number inside the route, from origin to destiny")
    kilometer = models.FloatField(verbose_name="Kilometer of the location inside the route", null=True)


class Manufacturer(models.Model):

    class Meta:
        app_label = 'infotrem'

    manufacturer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)


class ManufacturerInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    location = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)
