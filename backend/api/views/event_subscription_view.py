from django.db.models import QuerySet

from api.models import get_object_or_404, Event, Subscription
from api.serializers import SubscriptionSerializer
from api.services import policy
from .generic_model_view import ReadModelViewSet


class EventSubscriptionViewSet(ReadModelViewSet):
    permission_classes = [policy.IsLoggedIn, policy.IsAdminOrDeny]
    serializer_class = SubscriptionSerializer

    def get_queryset(self) -> QuerySet:
        event = get_object_or_404(Event.objects.all(), id=self.kwargs['event_id'])
        return Subscription.objects.filter(vacancy__event=event)
