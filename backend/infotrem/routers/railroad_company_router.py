from rest_framework import routers

from infotrem.views.railroad_company_view import RailroadCompanyViewSet, RailroadCompanyInformationViewSet, \
    RailroadCompanyPaintSchemeViewSet, RailroadCompanyPaintSchemeInformationViewSet

router = routers.SimpleRouter()
router.register(r'', RailroadCompanyViewSet, 'infotrem.railroad_company')
router.register(r'(?P<company_id>[^/.]+)/information', RailroadCompanyInformationViewSet, 'infotrem.railroad_company_information')
router.register(r'(?P<company_id>[^/.]+)/paint-schemes', RailroadCompanyPaintSchemeViewSet, 'infotrem.railroad_company_paint_scheme')
router.register(r'(?P<company_id>[^/.]+)/paint-schemes/(?P<paint_scheme_id>[^/.]+)/information', RailroadCompanyPaintSchemeInformationViewSet, 'infotrem.railroad_company_paint_scheme_information')
