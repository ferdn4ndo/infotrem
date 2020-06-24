from django.contrib.auth.models import User

from infotrem.serializers.rolling_stock import RollingStockSerializer


def add_url(user: User, item_type, name: str, photo_url: str):
    rolling_stock = RollingStockSerializer.get_or_create_from_name_and_type(
        name, item_type
    )


print('ToDo')
