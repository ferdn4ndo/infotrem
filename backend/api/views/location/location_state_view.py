from api.serializers.location.location_state_serializer import LocationStateSerializer
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.policies.is_admin_or_read_only_policy import IsAdminOrReadOnlyPolicy
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.location.location_state_model import LocationState


class LocationStateViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsAdminOrReadOnlyPolicy]
    serializer_class = LocationStateSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return LocationState.objects.all().order_by('abbrev', 'name')
