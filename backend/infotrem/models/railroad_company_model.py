import uuid

from django.db import models

from infotrem.models.information_model import Information


class RailroadCompany(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    abbrev = models.TextField(max_length=10)
    name = models.TextField(max_length=255)


class RailroadCompanyInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    railroad = models.ForeignKey(to=RailroadCompany, related_name='company_information', on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)


class RailroadCompanyPaintScheme(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    railroad = models.ForeignKey(to=RailroadCompany, on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name="Approx. date when the paint scheme has started", null=True)
    end_date = models.DateField(verbose_name="Approx. date when the paint scheme has ended", null=True)


class RailroadCompanyPaintSchemeInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paint_scheme = models.ForeignKey(to=RailroadCompanyPaintScheme, related_name='railroad_information', on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)
