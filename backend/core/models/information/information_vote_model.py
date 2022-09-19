from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.information.information_model import Information
from core.models.user.user_model import User


class InformationVote(GenericAuditedModel):

    BLANK_VOTE_VALUE = 0
    POSITIVE_VOTE_VALUE = 1
    NEGATIVE_VOTE_VALUE = -1

    class Meta:
        app_label = 'core'
        constraints = [
            models.UniqueConstraint(
                fields=['information', 'created_by'],
                name=_('Only one vote per user on each information')
            )
        ]

    information = models.ForeignKey(to=Information, related_name='votes', on_delete=models.CASCADE, editable=False)
    value = models.SmallIntegerField(default=0, verbose_name=_("Vote value"))

    @staticmethod
    def get_value_for_user(information: Information, user: User):
        try:
            vote = InformationVote.objects.get(information=information, created_by=user)

            return vote.value
        except InformationVote.DoesNotExist:
            return 0


class InformationVoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(InformationVote, InformationVoteAdmin)
