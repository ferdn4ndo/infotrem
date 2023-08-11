from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.policies.is_logged_in_or_read_only_policy import IsLoggedInOrReadOnlyPolicy
from api.serializers.album.album_serializer import AlbumSerializer
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import ensure_object_owner_or_deny
from core.models.album.album_model import Album
from core.services.album.album_service import AlbumService


class AlbumViewSet(FullCRUDListModelViewSet):
    """
    retrieve:
    Return the given album.

    list:
    Return a list of all the existing albums.

    create:
    Create a new album.
    """
    permission_classes = [IsLoggedInOrReadOnlyPolicy]
    serializer_class = AlbumSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Album.objects.none()

        return Album.objects.all().order_by('title')

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(user=request.user, model_type=Album, pk=kwargs['pk'])

        return super(AlbumViewSet, self).update(request=request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        ensure_object_owner_or_deny(user=request.user, model_type=Album, pk=kwargs['pk'])

        album = get_object_or_404(queryset=Album.objects.all(), pk=kwargs['pk'])

        AlbumService.delete_album(album=album)

        return Response(status=status.HTTP_204_NO_CONTENT)
