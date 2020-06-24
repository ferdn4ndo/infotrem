from rest_framework import routers

from infotrem.views.information import InformationViewSet

router = routers.SimpleRouter()
router.register(r'', InformationViewSet, 'infotrem.information')
