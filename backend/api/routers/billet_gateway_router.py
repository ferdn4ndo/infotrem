from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views import BilletGatewayViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=BilletGatewayViewSet,
    basename=RouteNames.ROUTE_BILLET_GATEWAY
)

urlpatterns = router.urls
