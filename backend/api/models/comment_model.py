from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_audited_model import GenericAuditedModel


class Comment(GenericAuditedModel):

    replies_to = models.ForeignKey(
        'self',
        null=True,
        verbose_name=_("The comment which this one is replying to"),
        on_delete=models.CASCADE
    )
    text = models.TextField(max_length=1024)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
