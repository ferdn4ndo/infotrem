from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .media_model import Media
from .user_model import User


class MediaReview(GenericAuditedModel):

    class ReviewDecision(models.TextChoices):
        REQUEST_CHANGES = 'REQUEST_CHANGES', \
                          _("Request changes (media will be temporary rejected until the author uploads it again)")
        APPROVED = 'APPROVED', _("Approved with no changes needed")
        REJECTED = 'REJECTED', _("Reject without possibility of updating the image")

    media_item = models.ForeignKey(to=Media, on_delete=models.CASCADE)
    moderator = models.ForeignKey(to=User, related_name='review_moderator', on_delete=models.SET_NULL, null=True)
    decision = models.CharField(max_length=64, choices=ReviewDecision.choices, null=True)
    comment = models.CharField(max_length=1024, null=True)


class MediaReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaReview, MediaReviewAdmin)

