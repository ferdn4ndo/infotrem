from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views import HealthViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=HealthViewSet,
    basename=RouteNames.ROUTE_HEALTH
)

urlpatterns = router.urls
