from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .comment_model import Comment
from .generic_audited_model import GenericAuditedModel
from .media_model import Media


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
