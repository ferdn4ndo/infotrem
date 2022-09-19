from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.album.album_model import Album
from core.models.generic_model import GenericModel
from core.models.user.user_model import User


class AlbumFavorite(GenericModel):

    album = models.ForeignKey(to=Album, on_delete=models.CASCADE, editable=False)
    favorited_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        editable=False,
        null=False,
        blank=False,
        related_name='album_favorite_creator',
        verbose_name=_("User who favorited the album"),
    )
    favorited_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date/time when the album was favorited")
    )


class AlbumFavoriteAdmin(admin.ModelAdmin):
    pass


admin.site.register(AlbumFavorite, AlbumFavoriteAdmin)
