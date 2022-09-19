from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers.album.album_serializer import AlbumSerializer
from api.services.policy import IsLoggedInOrReadOnly, ensure_object_owner_or_deny
from api.services.pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.album.album_model import Album


class AlbumViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnly]
    serializer_class = AlbumSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Album.objects.all().order_by('title')

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(request=request, model_type=Album, pk=kwargs['pk'])

        return super(AlbumViewSet, self).update(request=request, *args, **kwargs)
