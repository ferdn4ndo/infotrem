from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.policies.is_logged_in_or_read_only_policy import IsLoggedInOrReadOnlyPolicy
from api.serializers.location.location_information_serializer import LocationInformationSerializer
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import ensure_object_owner_or_deny
from core.models.location.location_information_model import LocationInformation
from core.models.location.location_model import Location


class LocationInformationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnlyPolicy]
    serializer_class = LocationInformationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        location = get_object_or_404(Location.objects.all(), id=self.kwargs['location_id'])

        return LocationInformation.objects.filter(location=location)

    def create(self, request: Request, *args, **kwargs) -> Response:
        request.data['location_id'] = self.kwargs['location_id']

        return super(LocationInformationViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(user=request.user, model_type=LocationInformation, pk=kwargs['pk'])

        instance = get_object_or_404(LocationInformation.objects.all(), pk=kwargs['pk'])
        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = instance.status

        request.data['location_id'] = self.kwargs['location_id']

        return super(LocationInformationViewSet, self).update(request=request, *args, **kwargs)
