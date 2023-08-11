from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from api.serializers.company.company_serializer import CompanySerializer
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import Company


class CompanyViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]
    serializer_class = CompanySerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Company.objects.none()

        return Company.objects.all().order_by('-created_at')
