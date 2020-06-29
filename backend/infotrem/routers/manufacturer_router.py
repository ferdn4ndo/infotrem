from rest_framework import routers

from infotrem.views.manufacturer_view import ManufacturerViewSet, ManufacturerInformationViewSet

router = routers.SimpleRouter()
router.register(r'manufacturers/', ManufacturerViewSet, 'infotrem.manufacturer')
router.register(r'manufacturers/(?P<manufacturer_id>[^/.]+)/information', ManufacturerInformationViewSet, 'infotrem.manufacturer_information')
