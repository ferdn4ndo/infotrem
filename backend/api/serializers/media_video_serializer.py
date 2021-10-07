from api.models import MediaVideo

from .generic_audited_model_serializer import GenericAuditedModelSerializer


class MediaVideoSerializer(GenericAuditedModelSerializer):

    class Meta:
        model = MediaVideo
        fields = [
            'id',
            'fps',
            'duration',
            'size_tag',
            'raw_height',
            'raw_width',
            'created_at',
            'updated_at',
        ]
