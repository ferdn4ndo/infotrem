from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_model import GenericModel
from api.models.track_gauge_model import TrackGauge


class FreightCarGrossWeightType(GenericModel):

    letter = models.CharField(max_length=1, unique=True, db_index=True, blank=False, null=False)
    max_gross_tons = models.FloatField(verbose_name=_("Max gross weight of the freight car type"))
    gauge = models.ForeignKey(to=TrackGauge, on_delete=models.PROTECT)


class FreightCarGrossWeightTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(FreightCarGrossWeightType, FreightCarGrossWeightTypeAdmin)



