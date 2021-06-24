from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views import SubscriptionViewSet, SubscriptionBilletViewSet, SubscriptionBilletDownloadViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=SubscriptionViewSet,
    basename=RouteNames.ROUTE_SUBSCRIPTION
)

router.register(
    prefix=r'(?P<subscription_id>[^/.]+)/billets',
    viewset=SubscriptionBilletViewSet,
    basename=RouteNames.ROUTE_SUBSCRIPTION_BILLET
)

router.register(
    prefix=r'(?P<subscription_id>[^/.]+)/billets/(?P<billet_id>[^/.]+)/download',
    viewset=SubscriptionBilletDownloadViewSet,
    basename=RouteNames.ROUTE_SUBSCRIPTION_BILLET_DOWNLOAD
)

urlpatterns = router.urls
