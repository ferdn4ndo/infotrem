from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_model import GenericModel
from .user_model import User


class GenericAuditedModel(GenericModel):
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_creator',
        verbose_name=_("Record creation user"),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Record creation timestamp"))
    updated_by = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_editor',
        verbose_name=_("Record last update user"),
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Record last update timestamp"), null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.id)

    objects = models.Manager()
