from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views.company.company_information_view import CompanyInformationViewSet
from api.views.company.company_paint_scheme_information_view import CompanyPaintSchemeInformationViewSet
from api.views.company.company_paint_scheme_view import CompanyPaintSchemeViewSet
from api.views.company.company_view import CompanyViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=CompanyViewSet,
    basename=RouteNames.ROUTE_COMPANY
)

router.register(
    prefix=r'(?P<company_id>[^/.]+)/information',
    viewset=CompanyInformationViewSet,
    basename=RouteNames.ROUTE_COMPANY_INFORMATION
)

router.register(
    prefix=r'(?P<company_id>[^/.]+)/paint-schemes',
    viewset=CompanyPaintSchemeViewSet,
    basename=RouteNames.ROUTE_COMPANY_PAINT_SCHEME
)

router.register(
    prefix=r'(?P<company_id>[^/.]+)/paint-schemes/(?P<paint_scheme_id>[^/.]+)/information',
    viewset=CompanyPaintSchemeInformationViewSet,
    basename=RouteNames.ROUTE_COMPANY_PAINT_SCHEME_INFORMATION
)

urlpatterns = router.urls
