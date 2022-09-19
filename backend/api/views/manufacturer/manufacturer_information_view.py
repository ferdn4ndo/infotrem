from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.serializers.manufacturer.manufacturer_information_serializer import ManufacturerInformationSerializer
from api.services.policy import IsLoggedInOrReadOnly, ensure_object_owner_or_deny
from api.services.pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.manufacturer.manufacturer_information_model import ManufacturerInformation
from core.models.manufacturer.manufacturer_model import Manufacturer


class ManufacturerInformationViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnly]
    serializer_class = ManufacturerInformationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        location = get_object_or_404(Manufacturer.objects.all(), id=self.kwargs['location_id'])

        return ManufacturerInformation.objects.filter(location=location)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(request=request, model_type=ManufacturerInformation, pk=kwargs['pk'])

        return super(ManufacturerInformationViewSet, self).update(request=request, *args, **kwargs)
