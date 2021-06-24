from api.models import Event, EventVacancy, get_object_or_404
from api.serializers import EventVacancySerializer
from api.services import policy
from .generic_model_view import FullCRUDListModelViewSet


class EventVacancyViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsAdminOrReadOnly]
    serializer_class = EventVacancySerializer

    def get_queryset(self):
        event = get_object_or_404(Event.objects.all(), id=self.kwargs['event_id'])
        return EventVacancy.objects.filter(event=event)
