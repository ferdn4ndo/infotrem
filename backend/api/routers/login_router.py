from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views.login.login_view import LoginViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=LoginViewSet,
    basename=RouteNames.ROUTE_LOGIN
)

urlpatterns = router.urls
