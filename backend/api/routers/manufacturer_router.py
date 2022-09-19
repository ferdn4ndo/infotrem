from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views.manufacturer.manufacturer_information_view import ManufacturerInformationViewSet
from api.views.manufacturer.manufacturer_view import ManufacturerViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=ManufacturerViewSet,
    basename=RouteNames.ROUTE_MANUFACTURER
)

router.register(
    prefix=r'(?P<manufacturer_id>[^/.]+)/information',
    viewset=ManufacturerInformationViewSet,
    basename=RouteNames.ROUTE_MANUFACTURER_INFORMATION
)

urlpatterns = router.urls
