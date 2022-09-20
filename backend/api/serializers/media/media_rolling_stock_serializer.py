from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.company.company_paint_scheme_serializer import CompanyPaintSchemeSerializer
from api.serializers.rolling_stock.rolling_stock_serializer import RollingStockSerializer
from api.serializers.user.user_serializer import UserSerializer
from core.models.media.media_rolling_stock_model import MediaRollingStock


class MediaRollingStockSerializer(GenericAuditedModelSerializer):
    rolling_stock = RollingStockSerializer()
    paint_scheme = CompanyPaintSchemeSerializer(required=False)
    created_by = UserSerializer()

    class Meta:
        model = MediaRollingStock
        fields = [
            'id',
            'media',
            'rolling_stock',
            'paint_scheme',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
        ]
