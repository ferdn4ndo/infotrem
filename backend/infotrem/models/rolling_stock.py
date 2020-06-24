import uuid

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from infotrem.models.information import Information
from infotrem.models.railroad import Manufacturer, RailroadCompany
from infotrem.models.track_gauge import TrackGauge


class RollingStockSigoRegional(models.Model):

    class Meta:
        app_label = 'infotrem'

    letter = models.CharField(max_length=1, primary_key=True)
    original_company = models.ForeignKey(to=RailroadCompany, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, verbose_name="Nome da regional")
    abbrev = models.CharField(max_length=20, null=True, verbose_name="Sigla da regional")


class RollingStock(models.Model):

    class Meta:
        app_label = 'infotrem'
        verbose_name = "Material Rodante"
        verbose_name_plural = "Materiais Rodantes"

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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100, choices=RollingStockType.choices)
    gauge = models.ForeignKey(to=TrackGauge, on_delete=models.PROTECT, null=True)
    is_sigo = models.BooleanField(verbose_name="If the rolling stock item is in SIGO standard", default=True)
    sigo_number = models.IntegerField(
        blank=False,
        null=True,
        verbose_name="SIGO range end number",
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(0)
        ]
    )
    regional = models.ForeignKey(to=RollingStockSigoRegional, on_delete=models.SET_NULL, null=True)
    painted_identifier = models.CharField(max_length=10, verbose_name="Painted identifier with letters/numbers/symbols")
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.SET_NULL, null=True)
    transformed_into = models.ForeignKey('self', null=True, verbose_name='Transformed Into', on_delete=models.SET_NULL)
    state = models.CharField(max_length=100, choices=RollingStockState.choices, default=RollingStockState.UNKNOWN)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="editor+")
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)

    def __str__(self):
        return self.sigo_number if self.is_sigo and self.sigo_number is not None else self.painted_identifier


class RollingStockSigoSeriesInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    sigo_start_number = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='SIGO range start number',
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(0)
        ]
    )
    sigo_end_number = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='SIGO range end number',
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(0)
        ]
    )
    information = models.ForeignKey(
        to=Information,
        on_delete=models.CASCADE,
        verbose_name="The information about the numeric range"
    )


class RollingStockInformation(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rolling_stock = models.ForeignKey(to=RollingStock, on_delete=models.CASCADE)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)
