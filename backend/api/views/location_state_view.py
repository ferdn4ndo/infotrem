from api.serializers.location_state_serializer import LocationStateSerializer
from api.services import pagination, policy
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.location.location_state_model import LocationState


class LocationStateViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsAdminOrReadOnly]
    serializer_class = LocationStateSerializer
    pagination_class = pagination.LargeResultsSetPagination

    def get_queryset(self):
        return LocationState.objects.all().order_by('abbrev', 'name')
