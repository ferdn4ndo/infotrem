from api.models import MediaDocument

from .generic_audited_model_serializer import GenericAuditedModelSerializer


class MediaDocumentSerializer(GenericAuditedModelSerializer):

    class Meta:
        model = MediaDocument
        fields = [
            'id',
            'pages',
            'black_and_white',
            'created_at',
            'updated_at',
        ]
