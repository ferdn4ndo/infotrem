from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .generic_audited_model import GenericAuditedModel
from .media_model import Media
from .company_paint_scheme_model import CompanyPaintScheme
from .rolling_stock_model import RollingStock


class MediaRollingStock(GenericAuditedModel):

    media = models.ForeignKey(to=Media, on_delete=models.CASCADE)
    rolling_stock = models.ForeignKey(to=RollingStock, on_delete=models.CASCADE)
    paint_scheme = models.ForeignKey(
        to=CompanyPaintScheme,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Paint scheme of the rolling stock presented in the media")
    )


class MediaRollingStockAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaRollingStock, MediaRollingStockAdmin)
