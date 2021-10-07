from rest_framework import serializers

from api.errors.internal_server_exception import InternalServerException
from api.models import Media, RollingStock, MediaImage, MediaVideo, MediaDocument

from .generic_audited_model_serializer import GenericAuditedModelSerializer
from .media_document_serializer import MediaDocumentSerializer
from .media_image_serializer import MediaImageSerializer
from .media_video_serializer import MediaVideoSerializer
from .rolling_stock_serializer import RollingStockSerializer
from .user_serializer import UserSerializer


class MediaSerializer(GenericAuditedModelSerializer):
    author = UserSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Media
        fields = [
            'id',
            'title',
            'type',
            'description',
            'thumbnail_filemgr_uuid',
            'status',
            'location',
            'known_author',
            'author_confirmed',
            'author',
            'original_url',
            'references',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
        ]

    def to_representation(self, instance: Media):
        instance_dict = super(MediaSerializer, self).to_representation(instance)
        instance_dict['metadata'] = {}

        if instance.type == Media.MediaType.IMAGE:
            model = MediaImage
            serializer = MediaImageSerializer
        elif instance.type == Media.MediaType.VIDEO:
            model = MediaVideo
            serializer = MediaVideoSerializer
        elif instance.type == Media.MediaType.DOCUMENT:
            model = MediaDocument
            serializer = MediaDocumentSerializer
        else:
            return instance_dict

        image_queryset = model.objects.filter(media_item=instance)
        if image_queryset.count() == 1:
            instance_dict['metadata'] = serializer(image_queryset[0]).data
        else:
            raise InternalServerException(
                "Database inconsistency: found {} {} objects for Media ID {}".format(
                    image_queryset.count(), model.__class__, instance.id,
                )
            )

        return instance_dict
