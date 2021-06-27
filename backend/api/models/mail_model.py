from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_model import GenericModel


class Mail(GenericModel):
    to = models.CharField(max_length=255, verbose_name=_("Destination e-mail address"))
    subject = models.CharField(max_length=255, verbose_name=_("Subject of the e-mail"))
    message_html = models.TextField(verbose_name=_("HTML content of the e-mail"))
    message_text = models.TextField(blank=True, null=True, verbose_name=_("Plain text content of the e-mail"))
    reply_to = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("E-mail address to reply"))
    sent = models.BooleanField(default=False, verbose_name=_("Flag to indicate if the e-mail was sent"))
    sent_at = models.DateTimeField(null=True, verbose_name=_("Date/time when the e-mail was sent"))
    server_response = models.TextField(null=True, verbose_name=_("SMTP server response when sending the e-mail"))


class MailAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mail, MailAdmin)
