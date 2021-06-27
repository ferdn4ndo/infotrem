from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .media_model import Media


class MediaImageSized(GenericAuditedModel):

    media_item = models.OneToOneField(to=Media, on_delete=models.CASCADE, primary_key=True, editable=False)
    filemgr_uuid = models.UUIDField(verbose_name=_("UUID of the file at FileMgr storage service"))
    size_tag = models.CharField(max_length=10, choices=Media.MediaSizeTag.choices, null=True)
    raw_height = models.PositiveIntegerField(verbose_name=_("Height of the sized media item"), null=True)
    raw_width = models.PositiveIntegerField(verbose_name=_("Width of the sized media item"), null=True)


class MediaImageSizedAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaImageSized, MediaImageSizedAdmin)
