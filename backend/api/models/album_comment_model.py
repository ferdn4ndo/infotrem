from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.album_model import Album
from api.models.comment_model import Comment
from api.models.generic_audited_model import GenericAuditedModel


class AlbumComment(GenericAuditedModel):

    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name=_("The album associated with the comment")
    )
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        editable=False,
        verbose_name=_("The comment associated with the album")
    )


class AlbumCommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(AlbumComment, AlbumCommentAdmin)
