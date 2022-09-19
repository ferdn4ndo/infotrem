from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.album.album_model import Album
from core.models.generic_audited_model import GenericAuditedModel
from core.models.media.media_model import Media


class AlbumMedia(GenericAuditedModel):

    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name=_("The album associated with the media item")
    )
    media = models.ForeignKey(
        to=Media,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name=_("The media item associated with the album")
    )


class AlbumMediaAdmin(admin.ModelAdmin):
    pass


admin.site.register(AlbumMedia, AlbumMediaAdmin)
