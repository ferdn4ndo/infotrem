from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.user.user_model import User


class Information(GenericAuditedModel):

    class InformationStatus(models.TextChoices):
        DISCUSSION = 'DISCUSSION', _("Information is still under discussion")
        ANALYSIS = 'ANALYSIS', _("Information is under analysis by a moderator")
        APPROVED = 'APPROVED', _("Information was approved by a moderator")
        REJECTED = 'REJECTED', _("Information was rejected by a moderator")

    class InformationType(models.TextChoices):
        OFFICIAL_DOCUMENT = 'OFFICIAL_DOCUMENT', _("Information from an official document")
        REPORT = 'REPORT', _("Information reported from somewhere/someone else")
        STORY = 'STORY', _("An story/memory informed by someone")

    type = models.CharField(max_length=64, choices=InformationType.choices)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    moderator = models.ForeignKey(to=User, related_name='information_moderator', on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=65535)
    status = models.CharField(max_length=10, choices=InformationStatus.choices, default=InformationStatus.ANALYSIS)
    references = models.TextField(max_length=1024, null=True)


class InformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Information, InformationAdmin)
