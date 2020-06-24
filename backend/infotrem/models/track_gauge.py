import uuid

from django.db import models


class TrackGauge(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.CharField(max_length=32, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    size = models.FloatField(verbose_name='Size of the gauge in meters', unique=True)
