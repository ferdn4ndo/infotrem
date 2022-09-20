from rest_framework import serializers

from api.serializers.information.information_serializer import InformationSerializer
from api.serializers.rolling_stock.rolling_stock_serializer import RollingStockSerializer
from core.models import RollingStockInformation, RollingStock


class RollingStockInformationSerializer(serializers.ModelSerializer):
    """Serializer for the RollingStock model"""
    rolling_stock = RollingStockSerializer()
    information = InformationSerializer()

    class Meta:
        model = RollingStockInformation
        fields = '__all__'

    @staticmethod
    def check_if_info_exists(rolling_stock: RollingStock, info_text: str):
        infos = RollingStockInformation.objects.filter(rolling_stock=rolling_stock)

        if not len(infos):
            return False

        texts = infos.values_list('information__content', flat=True)
        return info_text in texts
