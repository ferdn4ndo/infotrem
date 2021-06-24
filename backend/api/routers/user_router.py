from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views import UserViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=UserViewSet,
    basename=RouteNames.ROUTE_ME
)

urlpatterns = router.urls
