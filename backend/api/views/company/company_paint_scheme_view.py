from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from api.serializers.company.company_paint_scheme_serializer import CompanyPaintSchemeSerializer
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import Company, CompanyPaintScheme


class CompanyPaintSchemeViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]
    serializer_class = CompanyPaintSchemeSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        company = get_object_or_404(Company.objects.all(), id=self.kwargs['company_id'])

        return CompanyPaintScheme.objects.filter(company=company)

    def create(self, request: Request, *args, **kwargs) -> Response:
        request.data['company_id'] = self.kwargs['company_id']
        request.data['paint_scheme_id'] = self.kwargs['paint_scheme_id']

        return super(CompanyPaintSchemeViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        request.data['company_id'] = self.kwargs['company_id']
        request.data['paint_scheme_id'] = self.kwargs['paint_scheme_id']

        return super(CompanyPaintSchemeViewSet, self).update(request=request, *args, **kwargs)
