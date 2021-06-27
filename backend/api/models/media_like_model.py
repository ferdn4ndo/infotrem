from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_model import GenericModel
from .media_model import Media
from .user_model import User


class MediaLike(GenericModel):

    item = models.ForeignKey(to=Media, on_delete=models.CASCADE, editable=False)
    liked_by = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        editable=False,
        null=False,
        blank=False,
        related_name='media_favorite_creator',
        verbose_name=_("User who liked the media"),
    )
    liked_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date/time when the media was liked")
    )


class MediaLikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaLike, MediaLikeAdmin)
