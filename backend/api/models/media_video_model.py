from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .media_model import Media


class MediaVideo(GenericAuditedModel):

    media = models.OneToOneField(to=Media, on_delete=models.CASCADE, editable=False)
    fps = models.IntegerField(null=True, verbose_name=_("Framerate (frames per second) of the video"))
    duration = models.DurationField(null=True, verbose_name=_("Duration of the video"))
    size_tag = models.CharField(
        max_length=64,
        null=True,
        choices=Media.MediaSizeTag.choices,
        verbose_name=_("Biggest size tag of the media item")
    )
    raw_height = models.PositiveIntegerField(verbose_name="Height of the raw media item", null=True)
    raw_width = models.PositiveIntegerField(verbose_name="Width of the raw media item", null=True)


class MediaVideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaVideo, MediaVideoAdmin)
