from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.information.information_model import Information
from core.models.generic_model import GenericModel
from core.models.user.user_model import User


class InformationLike(GenericModel):

    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        editable=False,
        null=False,
        blank=False,
        related_name='likes',
        verbose_name=_("Information object which received the like"),
    )
    liked_by = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        editable=False,
        null=False,
        blank=False,
        related_name='information_like_creator',
        verbose_name=_("User who liked the information"),
    )
    liked_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date/time when the information was liked")
    )


class InformationLikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(InformationLike, InformationLikeAdmin)
