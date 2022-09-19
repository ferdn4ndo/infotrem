from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_model import GenericModel


class NonRevenueCarType(GenericModel):

    class RollingStockNonRevenueCarCategory(models.TextChoices):
        ELECTRICAL_MAINTENANCE = 'ELECTRICAL_MAINTENANCE', _("Equipment for Electrical Maintenance")
        RESCUE = 'RESCUE', _("Rescue Equipment")
        TRACK = 'TRACK', _("Track Equipment")
        VEGETATION = 'VEGETATION', _("Vegetation Equipment")
        OTHER = 'OTHER', _("Other Equipment")

    letters = models.CharField(max_length=5, unique=True, db_index=True, blank=False, null=False)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=RollingStockNonRevenueCarCategory.choices, null=True)


class NonRevenueCarTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(NonRevenueCarType, NonRevenueCarTypeAdmin)
