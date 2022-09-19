from api.serializers.location.location_serializer import LocationSerializer
from api.services.policy import IsStaffOrReadOnly
from api.services.pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.location.location_model import Location


class LocationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = LocationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Location.objects.all().order_by('abbrev', 'name')
