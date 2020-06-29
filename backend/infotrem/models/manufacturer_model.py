import uuid

from django.db import models

from infotrem.models.information_model import Information


class Manufacturer(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)


class ManufacturerInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manufacturer = models.ForeignKey(to=Manufacturer, related_name='information', on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)
