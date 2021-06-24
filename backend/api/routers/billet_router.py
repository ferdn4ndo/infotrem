from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views import BilletViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=BilletViewSet,
    basename=RouteNames.ROUTE_BILLET
)

# router.register(
#     prefix=r'(?P<billet_id>[^/.]+)/update',
#     viewset=BilletUpdateViewSet,
#     basename=RouteNames.ROUTE_BILLET_UPDATE
# )
#
# router.register(
#     prefix=r'(?P<billet_id>[^/.]+)/renew',
#     viewset=BilletRenewViewSet,
#     basename=RouteNames.ROUTE_BILLET_RENEW
# )

urlpatterns = router.urls
