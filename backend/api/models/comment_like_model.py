from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.comment_model import Comment
from api.models.generic_model import GenericModel
from api.models.user_model import User


class CommentLike(GenericModel):

    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name=_("The comment that was liked"),
    )
    liked_by = models.ForeignKey(
        to=User,
        unique=True,
        on_delete=models.CASCADE,
        editable=False,
        null=False,
        blank=False,
        related_name='comment_like_creator',
        verbose_name=_("User who liked the comment"),
    )
    liked_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date/time when the comment was liked"),
    )


class CommentLikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CommentLike, CommentLikeAdmin)
