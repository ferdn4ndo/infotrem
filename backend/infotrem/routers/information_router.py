from rest_framework import routers

from infotrem.views.information_view import InformationViewSet, InformationEffectViewSet

router = routers.SimpleRouter()
router.register(r'information/', InformationViewSet, 'infotrem.information')
router.register(r'information/(?P<information_id>[^/.]+)/effects', InformationEffectViewSet, 'infotrem.information_effect')
