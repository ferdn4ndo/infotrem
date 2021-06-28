from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .generic_model import GenericModel
from .freight_car_category_model import FreightCarCategory


class FreightCarType(GenericModel):

    letters = models.CharField(max_length=2, unique=True, db_index=True, blank=False, null=False)
    description = models.CharField(max_length=100, verbose_name=_("Description of the freight car gross weight type"))
    category = models.ForeignKey(to=FreightCarCategory, on_delete=models.PROTECT)


class FreightCarTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(FreightCarType, FreightCarTypeAdmin)



