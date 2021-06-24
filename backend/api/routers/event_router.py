from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views import EventViewSet, EventFileViewSet, EventFileDownloadViewSet, EventLinkViewSet, \
    EventSubscriptionViewSet, \
    EventVacancyViewSet, EventVacancySubscribeViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=EventViewSet,
    basename=RouteNames.ROUTE_EVENT
)

router.register(
    prefix=r'(?P<event_id>[^/.]+)/files',
    viewset=EventFileViewSet,
    basename=RouteNames.ROUTE_EVENT_FILE
)

router.register(
    prefix=r'(?P<event_id>[^/.]+)/files/(?P<file_id>[^/.]+)/download',
    viewset=EventFileDownloadViewSet,
    basename=RouteNames.ROUTE_EVENT_FILE_DOWNLOAD
)

router.register(
    prefix=r'(?P<event_id>[^/.]+)/links',
    viewset=EventLinkViewSet,
    basename=RouteNames.ROUTE_EVENT_LINK
)

router.register(
    prefix=r'(?P<event_id>[^/.]+)/subscriptions',
    viewset=EventSubscriptionViewSet,
    basename=RouteNames.ROUTE_EVENT_SUBSCRIPTION
)

router.register(
    prefix=r'(?P<event_id>[^/.]+)/vacancies',
    viewset=EventVacancyViewSet,
    basename=RouteNames.ROUTE_EVENT_VACANCY
)

router.register(
    prefix=r'(?P<event_id>[^/.]+)/vacancies/(?P<vacancy_id>[^/.]+)/subscribe',
    viewset=EventVacancySubscribeViewSet,
    basename=RouteNames.ROUTE_EVENT_VACANCY_SUBSCRIBE
)

urlpatterns = router.urls
