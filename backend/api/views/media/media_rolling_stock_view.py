from django.http import Http404
from rest_framework import generics, authentication
from rest_framework.response import Response

from api.serializers.media.media_rolling_stock_from_name_serializer import MediaRollingStockFromNameSerializer
from api.serializers.media.media_rolling_stock_serializer import MediaRollingStockSerializer
from core.models import MediaRollingStock, Media


class MediaRollingStockView(generics.ListCreateAPIView):
    queryset = MediaRollingStock.objects.all()
    serializer_class = MediaRollingStockFromNameSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_media_item(self, media_uuid):
        try:
            media_item = Media.objects.get(media_uuid=media_uuid)
        except Media.DoesNotExist:
            raise Http404

        return media_item

    def perform_create(self, serializer: MediaRollingStockSerializer):
        serializer.save(created_by=self.request.user)

    def list(self, request, *args, **kwargs):
        media_item = self.get_media_item(media_uuid=kwargs['media_uuid'])
        queryset = MediaRollingStock.objects.filter(media_item=media_item)
        serializer = MediaRollingStockSerializer(queryset, many=True)
        return Response(serializer.data)
