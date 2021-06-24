from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views import LocationCityViewSet, LocationStateViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=LocationStateViewSet,
    basename=RouteNames.ROUTE_STATE
)

router.register(
    prefix=r'(?P<state_id>[^/.]+)/cities',
    viewset=LocationCityViewSet,
    basename=RouteNames.ROUTE_STATE_CITY
)

urlpatterns = router.urls
