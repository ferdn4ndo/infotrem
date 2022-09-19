from api.serializers.manufacturer.manufacturer_serializer import ManufacturerSerializer
from api.services.policy import IsStaffOrReadOnly
from api.services.pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models.manufacturer.manufacturer_model import Manufacturer


class ManufacturerViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = ManufacturerSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Manufacturer.objects.all().order_by('short_name', 'full_name')
