from rest_framework.request import Request
from rest_framework.response import Response

from api.policies.is_logged_in_or_read_only_policy import IsLoggedInOrReadOnlyPolicy
from api.serializers.comment.comment_serializer import CommentSerializer
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import ensure_object_owner_or_deny
from core.models.comment.comment_model import Comment


class CommentViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnlyPolicy]
    serializer_class = CommentSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Comment.objects.all().order_by('-created_at')

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(user=request.user, model_type=Comment, pk=kwargs['pk'])

        return super(CommentViewSet, self).update(request=request, *args, **kwargs)
