from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.media_model import Media


class MediaVideo(GenericAuditedModel):

    media_item = models.OneToOneField(to=Media, on_delete=models.CASCADE, editable=False)
    fps = models.IntegerField(null=True, verbose_name=_("Framerate (frames per second) of the video"))
    duration = models.DurationField(null=True, verbose_name=_("Duration of the video"))


class MediaVideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaVideo, MediaVideoAdmin)