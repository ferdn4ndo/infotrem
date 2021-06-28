from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .location_model import Location
from .user_model import User


class Media(GenericAuditedModel):

    class MediaStatus(models.TextChoices):
        DRAFT = 'DRAFT', _("Draft (not ready for processing yet)")
        QUEUE = 'QUEUE', _("In the queue (waiting for processing)")
        PROCESSING = 'PROCESSING', _("Being processed by a worker")
        REVIEW = 'REVIEW', _("Media is waiting approval/reject by a moderator")
        PUBLISHED = 'PUBLISHED', _("Media was processed, approved and published")
        REJECTED_TEMP = 'REJECTED_TEMP', _("Media was temporary rejected, with a possible re-review")
        REJECTED_PERM = 'REJECTED_PERM', _("Media was permanently rejected")

    class MediaSizeTag(models.TextChoices):
        """ Height = math.ceil((Width*2/3)/32)*32 """
        SIZE_8K = 'SIZE_8K', _("8K (max 8192x5472 px @ 3:2, 45 Megapixels)")  # ~8K UHD
        SIZE_4K = 'SIZE_4K', _("4K (max 4096x2752 px @ 3:2, 11 Megapixels)")  # ~DCI 4K
        SIZE_3K = 'SIZE_3K', _("3K (max 3200x2144 px @ 3:2, 6.9 Megapixels)")  # ~QHD+
        SIZE_2K = 'SIZE_2K', _("2K (max 2048x1376 px @ 3:2, 2.8 Megapixels)")  # ~DCI 2K
        SIZE_1K = 'SIZE_1K', _("1K (max 1280x864 px @ 3:2, 1.1 Megapixels)")  # ~HD
        SIZE_THUMB_LARGE = 'SIZE_THUMB_LARGE', _("Large Thumbnail (960×640 px)")  # DVGA
        SIZE_THUMB_MEDIUM = 'SIZE_THUMB_MEDIUM', _("Medium Thumbnail (480×320 px)")  # WQVGA
        SIZE_THUMB_SMALL = 'SIZE_THUMB_SMALL', _("Small Thumbnail (240x160 px)")  # HQVGA

    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=65535, null=True)
    thumbnail_filemgr_uuid = models.UUIDField(verbose_name=_("UUID of the file at FileMgr storage service"))
    status = models.CharField(max_length=32, choices=MediaStatus.choices, default=MediaStatus.DRAFT)
    size_tag = models.CharField(
        max_length=64,
        null=True,
        choices=MediaSizeTag.choices,
        verbose_name=_("Biggest size tag of the media item")
    )
    raw_height = models.PositiveIntegerField(verbose_name="Height of the raw media item", null=True)
    raw_width = models.PositiveIntegerField(verbose_name="Width of the raw media item", null=True)
    location = models.ForeignKey(to=Location, on_delete=models.SET_NULL, null=True)
    known_author = models.BooleanField(default=False, verbose_name="If the author is known")
    author_confirmed = models.BooleanField(default=False, verbose_name="If the author is in the system and confirmed")
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="media_author+")
    original_url = models.TextField(max_length=255, null=True, verbose_name="Original URL, if downloaded")
    references = models.TextField(max_length=1024, null=True)


class MediaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Media, MediaAdmin)
