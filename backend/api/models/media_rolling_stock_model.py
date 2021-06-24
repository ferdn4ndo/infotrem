from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.media_model import Media
from api.models.company_paint_scheme_model import CompanyPaintScheme
from api.models.rolling_stock_model import RollingStock


class MediaRollingStock(GenericAuditedModel):

    media_item = models.ForeignKey(to=Media, on_delete=models.CASCADE)
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
