from rest_framework import routers

from infotrem.views.location_view import LocationViewSet, LocationTrackGaugeViewSet, LocationInformationViewSet

router = routers.SimpleRouter()
router.register(r'', LocationViewSet, 'infotrem.location')
router.register(r'(?P<location_id>[^/.]+)/track_gauges', LocationTrackGaugeViewSet, 'infotrem.location_track_gauge')
router.register(r'(?P<location_id>[^/.]+)/information', LocationInformationViewSet, 'infotrem.location_information')
