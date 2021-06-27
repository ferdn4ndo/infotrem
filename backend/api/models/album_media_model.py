from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .album_model import Album
from .generic_audited_model import GenericAuditedModel
from .media_model import Media


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
