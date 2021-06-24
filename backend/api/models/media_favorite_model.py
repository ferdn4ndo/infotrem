from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_model import GenericModel
from api.models.media_model import Media
from api.models.user_model import User


class MediaFavorite(GenericModel):

    media = models.ForeignKey(to=Media, on_delete=models.CASCADE, editable=False)
    favorited_by = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
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
