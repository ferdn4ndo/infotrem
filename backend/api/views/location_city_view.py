from api.models import get_object_or_404
from api.serializers.location_city_serializer import LocationCitySerializer
from api.services import pagination, policy
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.location.location_city_model import LocationCity
from core.models.location.location_state_model import LocationState


class LocationCityViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsAdminOrReadOnly]
    serializer_class = LocationCitySerializer
    pagination_class = pagination.LargeResultsSetPagination

    def get_queryset(self):
        state = get_object_or_404(LocationState.objects.all(), id=self.kwargs['state_id'])
        return LocationCity.objects.filter(state=state).order_by('name')
