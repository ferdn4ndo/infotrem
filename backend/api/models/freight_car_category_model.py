from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_model import GenericModel


class FreightCarCategory(GenericModel):

    letter = models.CharField(max_length=1, primary_key=True, unique=True, db_index=True, blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name=_("Name of the freight car category"))


class FreightCarCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(FreightCarCategory, FreightCarCategoryAdmin)


