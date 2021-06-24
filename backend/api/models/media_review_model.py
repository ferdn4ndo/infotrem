from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.media_model import Media
from api.models.user_model import User


class MediaReview(GenericAuditedModel):

    class ReviewDecision(models.TextChoices):
        REQUEST_CHANGES = _("Request changes (media will be temporary rejected until the author uploads it again)")
        APPROVED = _("Approved with no changes needed")
        REJECTED = _("Reject without possibility of updating the image")

    media_item = models.ForeignKey(to=Media, on_delete=models.CASCADE)
    moderator = models.ForeignKey(to=User, related_name='review_moderator', on_delete=models.SET_NULL, null=True)
    decision = models.CharField(max_length=10, choices=ReviewDecision.choices, null=True)
    comment = models.CharField(max_length=1024, null=True)


class MediaReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaReview, MediaReviewAdmin)

