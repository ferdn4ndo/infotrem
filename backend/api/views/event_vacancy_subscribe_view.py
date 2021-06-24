from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.errors import ConflictException
from api.models import Subscription, Event, EventVacancy
from api.serializers import SubscriptionSerializer
from api.services import policy, translation


class EventVacancySubscribeViewSet(ViewSet):
    permission_classes = [policy.IsLoggedIn]

    def create(self, request: Request, **kwargs):
        event = get_object_or_404(Event.objects.all(), id=kwargs['event_id'])

        if not event.is_open_for_subscriptions:
            raise ConflictException(translation.Messages.MSG_EVENT_NOT_OPEN_FOR_SUBSCRIPTIONS)

        vacancy = get_object_or_404(EventVacancy.objects.filter(event=event), id=self.kwargs['vacancy_id'])
        subscription = Subscription.subscribe_user(candidate=request.user, vacancy=vacancy)
        subscription.created_by = request.user
        serializer = SubscriptionSerializer(subscription)

        return Response(serializer.data)
