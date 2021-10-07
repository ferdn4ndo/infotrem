from api.models import AlbumComment

from .comment_serializer import CommentSerializer
from .generic_audited_model_serializer import GenericAuditedModelSerializer


class AlbumCommentSerializer(GenericAuditedModelSerializer):
    comment = CommentSerializer()

    class Meta:
        model = AlbumComment
        fields = [
            'id',
            'comment',
            'created_at',
            'updated_at',
        ]
