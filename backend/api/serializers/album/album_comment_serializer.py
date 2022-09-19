from rest_framework import serializers

from api.serializers.comment.comment_serializer import CommentSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models import Album
from core.models.album.album_comment_model import AlbumComment


class AlbumCommentSerializer(GenericAuditedModelSerializer):
    comment = CommentSerializer(required=True)
    album_id = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all(), required=False)
    comment_text = serializers.CharField(write_only=True, required=False, allow_blank=False)

    class Meta:
        model = AlbumComment
        fields = [
            'id',
            'album_id',
            'comment',
            'comment_text',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

    def create(self, validated_data):
        comment_data = validated_data.pop('comment')
        comment_serializer = CommentSerializer(data=comment_data)
        comment_serializer.is_valid(raise_exception=True)
        comment = comment_serializer.save()
        
        validated_data['comment'] = comment
        validated_data['album_id'] = validated_data['album_id'].id

        return super(AlbumCommentSerializer, self).create(validated_data=validated_data)

    def update(self, instance: AlbumComment, validated_data):
        comment_data = validated_data.pop('comment')

        previous_comment = instance.comment
        if previous_comment is not None:
            previous_comment.delete()

        comment_serializer = CommentSerializer(data=comment_data)
        comment_serializer.is_valid(raise_exception=True)
        comment = comment_serializer.save()

        validated_data['comment'] = comment
        validated_data['album_id'] = validated_data['album_id'].id

        return super(AlbumCommentSerializer, self).update(instance, validated_data=validated_data)
