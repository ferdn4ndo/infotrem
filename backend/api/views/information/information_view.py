from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers.information.information_serializer import InformationSerializer
from api.services.policy import IsLoggedInOrReadOnly, ensure_object_owner_or_deny
from api.services.pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.information.information_model import Information


class InformationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnly]
    serializer_class = InformationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Information.objects.all().order_by('-created_at')


    def create(self, request: Request, *args, **kwargs) -> Response:
        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = Information.InformationStatus.DISCUSSION

        return super(InformationViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(request=request, model_type=Information, pk=kwargs['pk'])

        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = Information.status

        return super(InformationViewSet, self).update(request=request, *args, **kwargs)
