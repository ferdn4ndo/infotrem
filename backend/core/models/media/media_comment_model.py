from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.comment.comment_model import Comment
from core.models.generic_audited_model import GenericAuditedModel
from core.models.media.media_model import Media


class MediaComment(GenericAuditedModel):

    media = models.ForeignKey(
        to=Media,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name=_("The media item associated with the comment")
    )
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name=_("The comment associated with the media item")
    )


class MediaCommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaComment, MediaCommentAdmin)
