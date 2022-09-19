from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_model import GenericModel


class FreightCarCategory(GenericModel):

    letter = models.CharField(max_length=1, unique=True, db_index=True, blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name=_("Name of the freight car category"))


class FreightCarCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(FreightCarCategory, FreightCarCategoryAdmin)
