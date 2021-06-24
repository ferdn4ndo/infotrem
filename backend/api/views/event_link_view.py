from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404, Event, Subscription, EventLink
from api.serializers import EventLinkSerializer
from api.services import policy
from api.views.generic_model_view import FullCRUDListModelViewSet


class EventLinkViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsAdminOrReadOnly]
    serializer_class = EventLinkSerializer

    def get_queryset(self) -> QuerySet:
        event = get_object_or_404(Event.objects.all(), id=self.kwargs['event_id'])
        queryset = EventLink.objects.filter(event=event, visibility=EventLink.LinkVisibility.EVERYONE)

        if not self.request.user or self.request.user.is_anonymous:
            return queryset

        if self.request.user.is_admin:
            return EventLink.objects.filter(event=event)

        if event in Subscription.get_user_subscribed_events(user=self.request.user):
            queryset = queryset | EventLink.objects.filter(event=event, visibility=EventLink.LinkVisibility.SUBSCRIBED)

        return queryset

    def create(self, request, *args, **kwargs):
        event = get_object_or_404(Event.objects.all(), id=self.kwargs['event_id'])
        request.data['event'] = str(event.id)

        return super(EventLinkViewSet, self).create(request=request, *args, **kwargs)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        return super(EventLinkViewSet, self).destroy(request=request, *args, **kwargs)
