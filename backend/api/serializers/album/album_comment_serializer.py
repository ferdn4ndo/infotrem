from rest_framework import serializers

from api.serializers.comment.comment_serializer import CommentSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models import Album
from core.models.album.album_comment_model import AlbumComment
from core.services.album.album_comment_service import AlbumCommentService


class AlbumCommentSerializer(GenericAuditedModelSerializer):
    comment = CommentSerializer(required=True)
    album_id = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all(), required=False)

    class Meta:
        model = AlbumComment
        fields = [
            'id',
            'album_id',
            'comment',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

    def create(self, validated_data):
        return AlbumCommentService.create_album_comment_from_data(input_data=validated_data)

    def update(self, instance: AlbumComment, validated_data):
        return AlbumCommentService.update_album_comment_from_data(
            input_data=validated_data,
            album_comment=instance
        )
