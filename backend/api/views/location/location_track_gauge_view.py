from api.models import get_object_or_404
from api.models.location_model import Location
from api.models.location_track_gauge_model import LocationTrackGauge
from api.serializers.location.location_track_gauge_serializer import LocationTrackGaugeSerializer
from api.services.policy import IsStaffOrReadOnly
from api.services.pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet


class LocationTrackGaugeViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = LocationTrackGaugeSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        location = get_object_or_404(Location.objects.all(), id=self.kwargs['location_id'])

        return LocationTrackGauge.objects.filter(location=location)
