from rest_framework import serializers

from core.models.media.media_model import Media
from core.models.media.media_rolling_stock_model import MediaRollingStock
from core.models.rolling_stock.rolling_stock_model import RollingStock
from .media_serializer import MediaSerializer
from .generic_audited_model_serializer import GenericAuditedModelSerializer
from .rolling_stock_serializer import RollingStockSerializer


class MediaItemRollingStockFromNameSerializer(GenericAuditedModelSerializer):
    media = MediaSerializer(allow_null=False, allow_blank=False)
    rolling_stock = RollingStockSerializer(read_only=True)
    rolling_stock_type = serializers.ChoiceField(
        choices=RollingStock.RollingStockType.choices,
        write_only=True,
        allow_null=False,
        allow_blank=False,
    )
    name = serializers.CharField(max_length=50, write_only=True, allow_blank=False, allow_null=False)

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
            'rolling_stock_type',
            'name',
        ]

    def create(self, validated_data):
        name = validated_data.get('name')
        rolling_stock_type = validated_data.get('rolling_stock_type')
        print(validated_data)

        try:
            media = Media.objects.get(pk=validated_data.get('media'))
        except Media.DoesNotExist:
            raise serializers.ValidationError("Media UUID is invalid")

        rolling_stock = RollingStockSerializer.get_or_create_from_name_and_type(name, rolling_stock_type)

        if MediaRollingStock.objects.filter(media=media, rolling_stock=rolling_stock).count() == 0:
            media_rolling_stock = MediaRollingStock(
                media=media,
                rolling_stock=rolling_stock,
                created_by=validated_data.get('created_by'),
            )
            media_rolling_stock.save()
        else:
            media_rolling_stock = MediaRollingStock.objects.filter(media=media, rolling_stock=rolling_stock).first()

        return media_rolling_stock
