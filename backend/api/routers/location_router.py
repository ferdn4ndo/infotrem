from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views.location.location_information_view import LocationInformationViewSet
from api.views.location.location_track_gauge_view import LocationTrackGaugeViewSet
from api.views.location.location_view import LocationViewSet


router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=LocationViewSet,
    basename=RouteNames.ROUTE_LOCATION
)

router.register(
    prefix=r'(?P<location_id>[^/.]+)/information',
    viewset=LocationInformationViewSet,
    basename=RouteNames.ROUTE_LOCATION_INFORMATION
)

router.register(
    prefix=r'(?P<location_id>[^/.]+)/track-gauges',
    viewset=LocationTrackGaugeViewSet,
    basename=RouteNames.ROUTE_LOCATION_TRACK_GAUGE
)

urlpatterns = router.urls
