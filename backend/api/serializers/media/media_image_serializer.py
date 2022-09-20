from core.models.media.media_image_model import MediaImage

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer


class MediaImageSerializer(GenericAuditedModelSerializer):

    class Meta:
        model = MediaImage
        fields = [
            'id',
            'focal_length',
            'aperture',
            'flash_fired',
            'iso',
            'orientation_angle',
            'is_flipped',
            'exposition',
            'datetime_taken',
            'camera_manufacturer',
            'camera_model',
            'exif_image_height',
            'exif_image_width',
            'size_tag',
            'raw_height',
            'raw_width',
            'created_at',
            'updated_at',
        ]
