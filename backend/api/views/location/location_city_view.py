from api.models import get_object_or_404
from api.serializers.location.location_city_serializer import LocationCitySerializer
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.policies.is_admin_or_read_only_policy import IsAdminOrReadOnlyPolicy

from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.location.location_city_model import LocationCity
from core.models.location.location_state_model import LocationState


class LocationCityViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsAdminOrReadOnlyPolicy]
    serializer_class = LocationCitySerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return LocationCity.objects.none()

        state = get_object_or_404(LocationState.objects.all(), id=self.kwargs['state_id'])

        return LocationCity.objects.filter(state=state).order_by('name')
