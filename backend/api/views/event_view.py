from django.contrib.auth.models import AnonymousUser

from api.models import Event
from api.serializers import EventSerializer
from api.services import policy
from .generic_model_view import FullCRUDListModelViewSet


class EventViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsAdminOrReadOnly]
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user

        if type(user) is not AnonymousUser and user and user.is_admin:
            return Event.objects.order_by('-registration_end_date').all()

        return Event.objects.filter(published=True).order_by('-registration_end_date').all()
