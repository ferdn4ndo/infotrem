from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.user.user_model import User


class Contact(GenericAuditedModel):

    class ContactType(models.TextChoices):
        BUG = 'BUG', _("Bug/problem report")
        FEEDBACK = 'FEEDBACK', _("Feedback (suggestions, critics, etc)")
        INCORRECT_INFO = 'INCORRECT_INFO', _("Incorrect information presented on the website")
        AUTHOR_REQUEST = 'AUTHOR_REQUEST', _("Author definition and copyright issues")
        DATA_REMOVAL = 'DATA_REMOVAL', _("Request to remove data")

    type = models.CharField(max_length=64, choices=ContactType.choices)
    user = models.ForeignKey(to=User, related_name='contact_user', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    message = models.TextField(max_length=5000, null=True, blank=True)


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)
