from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.policies.is_logged_in_or_read_only_policy import IsLoggedInOrReadOnlyPolicy
from api.serializers.album.album_comment_serializer import AlbumCommentSerializer
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.services.policy import ensure_object_owner_or_deny
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.album.album_comment_model import AlbumComment
from core.models.album.album_model import Album


class AlbumCommentViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnlyPolicy]
    serializer_class = AlbumCommentSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        album = get_object_or_404(Album.objects.all(), id=self.kwargs['album_id'])

        return AlbumComment.objects.filter(album=album).order_by('-created_at')

    def create(self, request: Request, *args, **kwargs) -> Response:
        request.data['album_id'] = kwargs['album_id']

        return super(AlbumCommentViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(request=request, model_type=AlbumComment, pk=kwargs['pk'])

        request.data['album_id'] = kwargs['album_id']

        return super(AlbumCommentViewSet, self).update(request=request, *args, **kwargs)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        album_comment = get_object_or_404(AlbumComment.objects.all(), id=self.kwargs['pk'])

        return self.remove_instance_and_return_204(album_comment.comment)
