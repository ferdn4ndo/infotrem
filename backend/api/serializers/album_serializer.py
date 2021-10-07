from rest_framework import serializers

from api.models import Album, AlbumFavorite, AlbumLike

from .album_comment_serializer import AlbumCommentSerializer
from .generic_audited_model_serializer import GenericAuditedModelSerializer


class AlbumSerializer(GenericAuditedModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_favorites = serializers.SerializerMethodField()
    comments = AlbumCommentSerializer(many=True)

    class Meta:
        model = Album
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'updated_at',
            'total_likes',
            'total_favorites',
            'comments',
        ]

    @staticmethod
    def get_total_likes(obj):
        return AlbumLike.objects.filter(album=obj).count()

    @staticmethod
    def get_total_favorites(obj):
        return AlbumFavorite.objects.filter(album=obj).count()
