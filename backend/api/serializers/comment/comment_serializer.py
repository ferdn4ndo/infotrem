from rest_framework import serializers


from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.recursive_field_serializer import RecursiveField
from core.models.comment.comment_like_model import CommentLike
from core.models.comment.comment_model import Comment


class CommentSerializer(GenericAuditedModelSerializer):
    replies = RecursiveField(many=True, read_only=True)
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'replies_to',
            'text',
            'replies',
            'total_likes',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

    @staticmethod
    def get_total_likes(obj):
        return CommentLike.objects.filter(comment=obj).count()
