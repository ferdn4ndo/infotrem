from rest_framework.request import Request
from rest_framework.response import Response

from api.policies.is_logged_in_or_read_only_policy import IsLoggedInOrReadOnlyPolicy
from api.serializers.information.information_serializer import InformationSerializer
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import ensure_object_owner_or_deny
from core.models.information.information_model import Information


class InformationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnlyPolicy]
    serializer_class = InformationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Information.objects.none()

        return Information.objects.all().order_by('-created_at')

    def create(self, request: Request, *args, **kwargs) -> Response:
        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = Information.InformationStatus.DISCUSSION

        return super(InformationViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(user=request.user, model_type=Information, pk=kwargs['pk'])

        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = Information.status

        return super(InformationViewSet, self).update(request=request, *args, **kwargs)