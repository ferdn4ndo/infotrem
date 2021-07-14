from rest_framework import serializers

from api.models import Comment, CommentLike

from .generic_audited_model_serializer import GenericAuditedModelSerializer
from .recursive_field_serializer import RecursiveField


class CommentSerializer(GenericAuditedModelSerializer):
    replies = RecursiveField(many=True)
    total_likes = serializers.SerializerMethodField()
    total_favorites = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'replies_to',
            'text',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
        ]

    @staticmethod
    def get_total_likes(obj):
        return CommentLike.objects.filter(album=obj).count()

