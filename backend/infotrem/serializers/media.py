from rest_framework import serializers

from infotrem.models.media import ImageMediaItem, MediaItem, MediaItemRollingStock
from infotrem.models.rolling_stock import RollingStock
from infotrem.models.storage import StorageFile
from infotrem.serializers.railroad import RailroadPaintSchemeSerializer
from infotrem.serializers.rolling_stock import RollingStockSerializer
from infotrem.serializers.storage import StorageFileSerializer
from infotrem.serializers.user import UserSerializer
from infotrem.validators.file import FileValidator

validate_file = FileValidator(
    max_size=1024 * 100,
    content_types=(
        'image/jpeg',
        'image/png',
        'image/tiff',
        'image/bmp',
        'image/gif',
    )
)


# class MediaUploadSerializer(serializers.Serializer, ABC):
#     file = serializers.FileField(validators=[validate_file])


class ImageMediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageMediaItem
        exclude = ['media_item']


class MediaItemSerializer(serializers.ModelSerializer):
    file_raw = StorageFileSerializer()
    author = UserSerializer()
    created_by = UserSerializer()

    class Meta:
        model = MediaItem
        fields = '__all__'

    def to_representation(self, instance: MediaItem):
        instance_dict = super(MediaItemSerializer, self).to_representation(instance)
        instance_dict['metadata'] = None
        if instance.file_raw.file_type == StorageFile.FileType.TYPE_IMAGE:
            image_queryset = ImageMediaItem.objects.filter(media_item=instance)
            if len(image_queryset) == 1:
                instance_dict['metadata'] = ImageMediaItemSerializer(image_queryset[0]).data

        return instance_dict


class MediaItemRollingStockSerializer(serializers.ModelSerializer):
    media_item = MediaItemSerializer()
    rolling_stock = RollingStockSerializer()
    paint_scheme = RailroadPaintSchemeSerializer(required=False)
    created_by = UserSerializer()

    class Meta:
        model = MediaItemRollingStock
        fields = '__all__'


class MediaItemRollingStockFromNameSerializer(serializers.Serializer):
    media_uuid = serializers.CharField()
    rolling_stock_type = serializers.ChoiceField(choices=RollingStock.RollingStockType.choices)
    name = serializers.CharField(max_length=50)
    created_by = UserSerializer(required=False)

    def create(self, validated_data):
        name = validated_data.get('name')
        rolling_stock_type = validated_data.get('rolling_stock_type')
        print(validated_data)

        try:
            media_item = MediaItem.objects.get(pk=validated_data.get('media_uuid'))
        except MediaItem.DoesNotExist:
            raise serializers.ValidationError("Media item UUID is invalid")

        rolling_stock = RollingStockSerializer.get_or_create_from_name_and_type(name, rolling_stock_type)

        rolling_stock_item = MediaItemRollingStock(
            media_item=media_item,
            rolling_stock=rolling_stock,
            created_by=validated_data.get('created_by'),
        )
        rolling_stock_item.save()

        return rolling_stock_item

    def to_representation(self, instance: MediaItemRollingStock):
        """Convert the MediaItemRollingStock to the serializer fields"""

        ret = {
            'media_id': instance.media_item.media_id,
            'rolling_stock_type': 'test',
            'name': 'test',
            'created_by': 'test',
        }

        return ret

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
