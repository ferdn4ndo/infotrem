from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views.information.information_effect_view import InformationEffectViewSet
from api.views.information.information_vote_view import InformationVoteViewSet
from api.views.information.information_view import InformationViewSet


router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=InformationViewSet,
    basename=RouteNames.ROUTE_INFORMATION
)

router.register(
    prefix=r'(?P<information_id>[0-9a-f-]+)/effects',
    viewset=InformationEffectViewSet,
    basename=RouteNames.ROUTE_INFORMATION_EFFECT
)

router.register(
    prefix=r'(?P<information_id>[0-9a-f-]+)/votes',
    viewset=InformationVoteViewSet,
    basename=RouteNames.ROUTE_INFORMATION_VOTE
)

urlpatterns = router.urls
