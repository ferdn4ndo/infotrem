import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _


class Information(models.Model):
    class InformationStatus(models.TextChoices):
        DISCUSSION = 'DISCUSSION', _('Discussion')
        ANALYSIS = 'ANALYSIS', _('Under Analysis')
        APPROVED = 'APPROVED', _('Approved')
        REJECTED = 'REJECTED', _('Rejected')

    information_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=65535)
    status = models.CharField(max_length=10, choices=InformationStatus.choices, default=InformationStatus.ANALYSIS)
    references = models.TextField(max_length=1024, null=True)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=datetime.utcnow, editable=False)
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="editor+")
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)

    class Meta:
        app_label = 'infotrem'


class InformationEffect(models.Model):
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)
    field_name = models.TextField(max_length=255)
    old_value = models.TextField(max_length=1024)
    new_value = models.TextField(max_length=1024)

    class Meta:
        app_label = 'infotrem'
