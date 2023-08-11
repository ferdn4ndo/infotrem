from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_model import GenericModel
from core.models.media.media_model import Media
from core.models.user.user_model import User


class MediaFavorite(GenericModel):

    media = models.ForeignKey(to=Media, on_delete=models.CASCADE, editable=False)
    favorited_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        editable=False,
        null=False,
        blank=False,
        related_name='media_favorite_creator',
        verbose_name=_("User who favorited the media"),
    )
    favorited_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date/time when the media was favorited")
    )


class MediaFavoriteAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaFavorite, MediaFavoriteAdmin)