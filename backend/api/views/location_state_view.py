from api.models import LocationState, get_object_or_404
from api.serializers import LocationStateSerializer
from api.services import pagination, policy
from .generic_model_view import FullCRUDListModelViewSet


class LocationStateViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsAdminOrReadOnly]
    serializer_class = LocationStateSerializer
    pagination_class = pagination.LargeResultsSetPagination

    def get_queryset(self):
        return LocationState.objects.all().order_by('abbrev', 'name')
