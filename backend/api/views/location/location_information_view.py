from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.serializers.location.location_information_serializer import LocationInformationSerializer
from api.services.policy import IsLoggedInOrReadOnly, ensure_object_owner_or_deny
from api.services.pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.location.location_information_model import LocationInformation
from core.models.location.location_model import Location


class LocationInformationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnly]
    serializer_class = LocationInformationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        location = get_object_or_404(Location.objects.all(), id=self.kwargs['location_id'])

        return LocationInformation.objects.filter(location=location)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(request=request, model_type=LocationInformation, pk=kwargs['pk'])

        return super(LocationInformationViewSet, self).update(request=request, *args, **kwargs)
