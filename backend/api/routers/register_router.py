from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views.register_view import RegisterViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=RegisterViewSet,
    basename=RouteNames.ROUTE_REGISTER
)

urlpatterns = router.urls
