from api.serializers.location.location_serializer import LocationSerializer
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.location.location_model import Location


class LocationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]
    serializer_class = LocationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Location.objects.all().order_by('abbrev', 'name')
