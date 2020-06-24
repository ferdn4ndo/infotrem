import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Information(models.Model):
    class InformationStatus(models.TextChoices):
        DISCUSSION = 'DISCUSSION', _('Discussion')
        ANALYSIS = 'ANALYSIS', _('Under Analysis')
        APPROVED = 'APPROVED', _('Approved')
        REJECTED = 'REJECTED', _('Rejected')

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=65535)
    status = models.CharField(max_length=10, choices=InformationStatus.choices, default=InformationStatus.ANALYSIS)
    references = models.TextField(max_length=1024, null=True)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="editor+")
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)

    @property
    def votes_up(self):
        return len(InformationVote.objects.filter(information=self.id, value__gt=0))

    @property
    def votes_down(self):
        return len(InformationVote.objects.filter(information=self.id, value__lt=0))

    @property
    def votes_sum(self):
        return InformationVote.objects.filter(information=self.id).aggregate(Sum('value'))['value__sum']


class InformationEffect(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    information = models.ForeignKey(to=Information, related_name='effects', on_delete=models.CASCADE)
    field_name = models.TextField(max_length=255)
    old_value = models.TextField(max_length=1024)
    new_value = models.TextField(max_length=1024)


class InformationVote(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    information = models.ForeignKey(to=Information, related_name='votes', on_delete=models.CASCADE)
    value = models.SmallIntegerField(default=0, verbose_name="Vote value ")
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="editor+")
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)
