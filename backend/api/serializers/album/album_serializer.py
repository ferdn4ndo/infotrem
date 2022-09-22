from rest_framework import serializers

from api.serializers.album.album_comment_serializer import AlbumCommentSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models.album.album_favorite_model import AlbumFavorite
from core.models.album.album_like_model import AlbumLike
from core.models.album.album_model import Album


class AlbumSerializer(GenericAuditedModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_favorites = serializers.SerializerMethodField()
    album_comments = AlbumCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            'id',
            'title',
            'description',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
            'total_likes',
            'total_favorites',
            'album_comments',
        ]

    @staticmethod
    def get_total_likes(obj):
        return AlbumLike.objects.filter(album=obj).count()

    @staticmethod
    def get_total_favorites(obj):
        return AlbumFavorite.objects.filter(album=obj).count()
