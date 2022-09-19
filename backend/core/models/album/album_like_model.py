from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.album.album_model import Album
from core.models.generic_model import GenericModel
from core.models.user.user_model import User


class AlbumLike(GenericModel):

    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name=_("The album that was liked"),
    )
    liked_by = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        editable=False,
        null=False,
        blank=False,
        related_name='album_like_creator',
        verbose_name=_("User who liked the album"),
    )
    liked_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date/time when the album was liked"),
    )


class AlbumLikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(AlbumLike, AlbumLikeAdmin)
