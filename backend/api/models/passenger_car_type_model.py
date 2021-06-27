from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_model import GenericModel


class PassengerCarType(GenericModel):

    letter = models.CharField(max_length=1, unique=True, db_index=True, blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name=_("Name of the type of the passenger cars"))


class PassengerCarTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(PassengerCarType, PassengerCarTypeAdmin)
