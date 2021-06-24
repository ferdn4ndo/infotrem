from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.manufacturer_model import Manufacturer
from api.models.sigo_regional_model import SigoRegional
from api.models.track_gauge_model import TrackGauge


class RollingStock(GenericAuditedModel):

    class RollingStockType(models.TextChoices):
        LOCOMOTIVE = 'LOCOMOTIVE', _("Locomotive")
        FREIGHT_CAR = 'FREIGHT_CAR', _("Freight Car")
        PASSENGER_CAR = 'PASSENGER_CAR', _("Passenger Car")
        RAILCAR_COACH_MU = 'RAILCAR_COACH_MU', _("Railcar, Rail motor coach or Multiple Unit")
        NON_REVENUE_CAR = 'NON_REVENUE_CAR', _("Non-revenue Car")
        OTHERS = 'OTHERS', _("Others (non-listed)")

    class RollingStockPrimeMover(models.TextChoices):
        MANUAL = 'MANUAL', _("Manual")
        STEAM = 'STEAM', _("Steam")
        DIESEL_MECHANICAL = 'DIESEL_MECHANICAL', _("Diesel-mechanical")
        DIESEL_ELECTRIC = 'DIESEL_ELECTRIC', _("Diesel–electric")
        DIESEL_HYDRAULIC = 'DIESEL_HYDRAULIC', _("Diesel-hydraulic")
        ELECTRIC = 'ELECTRIC', _("Electric")
        GAS_TURBINE = 'GAS_TURBINE', _("Gas turbine")
        HYBRID = 'HYBRID', _("Hybrid")
        OTHERS = 'OTHERS', _("Others types")

    class RollingStockState(models.TextChoices):
        ACTIVE = 'ACTIVE', _("Active")
        INOPERATIVE = 'INOPERATIVE', _("Inoperative")
        DISMANTLED = 'DISMANTLED', _("Dismantled")
        TRANSFORMED = 'TRANSFORMED', _("Transformed")
        UNKNOWN = 'UNKNOWN', _("Unknown")

    type = models.CharField(max_length=100, choices=RollingStockType.choices)
    gauge = models.ForeignKey(to=TrackGauge, on_delete=models.PROTECT, null=True)
    is_sigo = models.BooleanField(verbose_name=_("If the rolling stock item is in SIGO standard"), default=True)
    sigo_number = models.IntegerField(
        blank=False,
        null=True,
        verbose_name=_("SIGO range end number"),
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(0)
        ]
    )
    regional = models.ForeignKey(to=SigoRegional, on_delete=models.SET_NULL, null=True)
    painted_identifier = models.CharField(
        max_length=20,
        verbose_name=_("Painted identifier with letters/numbers/symbols"),
    )
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.SET_NULL, null=True)
    serial_number = models.CharField(max_length=200, null=True, verbose_name=_("Serial number of the rolling stock"))
    build_year = models.IntegerField(null=True, verbose_name=_("Year when it was built"))
    transformed_into = models.ForeignKey(
        to='self',
        null=True,
        verbose_name=_("Rolling stock which this one was transformed into"),
        on_delete=models.SET_NULL
    )
    state = models.CharField(max_length=100, choices=RollingStockState.choices, default=RollingStockState.UNKNOWN)

    def __str__(self):
        return self.sigo_number if self.is_sigo and self.sigo_number is not None else self.painted_identifier


class RollingStockAdmin(admin.ModelAdmin):
    pass


admin.site.register(RollingStock, RollingStockAdmin)
