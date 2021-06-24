from uuid import uuid4

from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.user_model import User


class UserToken(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_("User that has the token"))
    token = models.CharField(
        max_length=255,
        unique=True,
        editable=False,
        verbose_name=_("Token used to login (from uServer-Auth)")
    )
    issued_at = models.DateTimeField(
        verbose_name=_("Date when the token was issued by uServer-Auth"),
        editable=False
    )
    expires_at = models.DateTimeField(
        verbose_name=_("Date when the token expires (defined by uServer-Auth)"),
        editable=False
    )


class UserTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserToken, UserTokenAdmin)
