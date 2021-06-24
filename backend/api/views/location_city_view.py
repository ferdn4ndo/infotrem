from api.models import LocationCity, LocationState, get_object_or_404
from api.serializers import LocationCitySerializer
from api.services import pagination, policy
from .generic_model_view import FullCRUDListModelViewSet


class LocationCityViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsAdminOrReadOnly]
    serializer_class = LocationCitySerializer
    pagination_class = pagination.LargeResultsSetPagination

    def get_queryset(self):
        state = get_object_or_404(LocationState.objects.all(), id=self.kwargs['state_id'])
        return LocationCity.objects.filter(state=state).order_by('name')
