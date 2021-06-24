from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.comment_model import Comment
from api.models.generic_audited_model import GenericAuditedModel
from api.models.media_model import Media


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
