from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from api.serializers.company.company_paint_scheme_information_serializer import CompanyPaintSchemeInformationSerializer
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import CompanyPaintScheme, CompanyPaintSchemeInformation, ensure_object_owner_or_deny


class CompanyPaintSchemeInformationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]
    serializer_class = CompanyPaintSchemeInformationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return CompanyPaintSchemeInformation.objects.none()

        paint_scheme = get_object_or_404(CompanyPaintScheme.objects.all(), id=self.kwargs['paint_scheme_id'])

        return CompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)

    def create(self, request: Request, *args, **kwargs) -> Response:
        request.data['paint_scheme_id'] = self.kwargs['paint_scheme_id']

        return super(CompanyPaintSchemeInformationViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(user=request.user, model_type=CompanyPaintSchemeInformation, pk=kwargs['pk'])

        instance = get_object_or_404(CompanyPaintSchemeInformation.objects.all(), pk=kwargs['pk'])
        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = instance.status

        request.data['paint_scheme_id'] = self.kwargs['paint_scheme_id']

        return super(CompanyPaintSchemeInformationViewSet, self).update(request=request, *args, **kwargs)
