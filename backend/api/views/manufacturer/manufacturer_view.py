from api.serializers.manufacturer.manufacturer_serializer import ManufacturerSerializer
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.manufacturer.manufacturer_model import Manufacturer


class ManufacturerViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]
    serializer_class = ManufacturerSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Manufacturer.objects.all().order_by('short_name', 'full_name')
