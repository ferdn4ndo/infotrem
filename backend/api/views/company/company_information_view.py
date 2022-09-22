from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from api.serializers.company.company_information_serializer import CompanyInformationSerializer
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import Company, CompanyInformation, ensure_object_owner_or_deny


class CompanyInformationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]
    serializer_class = CompanyInformationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        company = get_object_or_404(Company.objects.all(), id=self.kwargs['company_id'])

        return CompanyInformation.objects.filter(company=company)

    def create(self, request: Request, *args, **kwargs) -> Response:
        request.data['company_id'] = self.kwargs['company_id']

        return super(CompanyInformationViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(user=request.user, model_type=CompanyInformation, pk=kwargs['pk'])

        instance = get_object_or_404(CompanyInformation.objects.all(), pk=kwargs['pk'])
        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = instance.status

        request.data['company_id'] = self.kwargs['company_id']

        return super(CompanyInformationViewSet, self).update(request=request, *args, **kwargs)
