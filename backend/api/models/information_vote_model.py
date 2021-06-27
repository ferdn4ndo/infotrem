from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .information_model import Information
from .user_model import User


class InformationVote(GenericAuditedModel):

    BLANK_VOTE_VALUE = 0
    POSITIVE_VOTE_VALUE = 1
    NEGATIVE_VOTE_VALUE = -1

    class Meta:
        app_label = 'api'
        constraints = [
            models.UniqueConstraint(
                fields=['information', 'voter'],
                name=_('Only one vote per user on each information')
            )
        ]

    information = models.ForeignKey(to=Information, related_name='votes', on_delete=models.CASCADE, editable=False)
    value = models.SmallIntegerField(default=0, verbose_name=_('Vote value'))
    voter = models.ForeignKey(to=User, null=True, related_name='user_voter+', on_delete=models.CASCADE, editable=False)


class InformationVoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(InformationVote, InformationVoteAdmin)
