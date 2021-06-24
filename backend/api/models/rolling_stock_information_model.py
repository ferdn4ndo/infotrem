from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.information_model import Information
from api.models.rolling_stock_model import RollingStock


class RollingStockInformation(GenericAuditedModel):
    rolling_stock = models.ForeignKey(
        to=RollingStock,
        on_delete=models.CASCADE,
        verbose_name=_("Rolling stock which holds the information"),
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name=_("Information associated with the rolling stock"),
    )


class RollingStockInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(RollingStockInformation, RollingStockInformationAdmin)



