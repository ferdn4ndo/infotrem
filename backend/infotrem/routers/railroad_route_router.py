from rest_framework import routers

from infotrem.views.railroad_route_view import RailroadRouteViewSet, RailroadRouteInformationViewSet, \
    RailroadRouteSectionViewSet, RailroadRouteSectionInformationViewSet, RailroadRouteSectionLocationViewSet, \
    RailroadRouteSectionPathViewSet

router = routers.SimpleRouter()
router.register(
    prefix=r'',
    viewset=RailroadRouteViewSet,
    basename='infotrem.railroad_route'
)
router.register(
    prefix=r'(?P<route_id>[^/.]+)/information',
    viewset=RailroadRouteInformationViewSet,
    basename='infotrem.railroad_route_information',
)
router.register(
    prefix=r'(?P<route_id>[^/.]+)/sections',
    viewset=RailroadRouteSectionViewSet,
    basename='infotrem.railroad_route_section',
)
router.register(
    prefix=r'(?P<route_id>[^/.]+)/sections/(?P<section_id>[^/.]+)/information',
    viewset=RailroadRouteSectionInformationViewSet,
    basename='infotrem.railroad_route_section_information',
)
router.register(
    prefix=r'(?P<route_id>[^/.]+)/sections/(?P<section_id>[^/.]+)/locations',
    viewset=RailroadRouteSectionLocationViewSet,
    basename='infotrem.railroad_route_section_location',
)
router.register(
    prefix=r'(?P<route_id>[^/.]+)/sections/(?P<section_id>[^/.]+)/paths',
    viewset=RailroadRouteSectionPathViewSet,
    basename='infotrem.railroad_route_section_location',
)
