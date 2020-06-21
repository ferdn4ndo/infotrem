from django.contrib.auth.models import User

from infotrem.models.information import Information
from infotrem.models.rolling_stock import RollingStock, RollingStockInformation
from infotrem.serializers.rolling_stock import RollingStockSerializer


def add_url(user: User, item_type, name: str, photo_url: str):
    rolling_stock = RollingStockSerializer.get_or_create_from_name_and_type(
        name, item_type
    )

    information = Information.objects.create(
        author=user,
        content="Fotografia baixada de {}".format(photo_url),
        status=Information.InformationStatus.DISCUSSION,
    )
    information.save()

    rolling_stock_information = RollingStockInformation.objects.create(
        rolling_stock=rolling_stock,
        information=information
    )
    rolling_stock_information.save()


def run():
    rstype = RollingStock.RollingStockType

