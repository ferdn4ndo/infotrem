from django.db.models import QuerySet
from rest_framework.authentication import get_authorization_header
from rest_framework.request import Request
from rest_framework.response import Response

from api.errors import NotFoundException
from api.models import get_object_or_404, Event, Subscription, EventFile
from api.serializers import EventFileSerializer
from api.services import policy, filemgr_service
from api.views.generic_model_view import FullCRUDListModelViewSet


class EventFileViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsAdminOrReadOnly]
    serializer_class = EventFileSerializer

    def get_queryset(self) -> QuerySet:
        event = get_object_or_404(Event.objects.all(), id=self.kwargs['event_id'])
        queryset = EventFile.objects.filter(event=event, visibility=EventFile.FileVisibility.EVERYONE)

        if not self.request.user or self.request.user.is_anonymous:
            return queryset

        if self.request.user.is_admin:
            return EventFile.objects.filter(event=event)

        if event in Subscription.get_user_subscribed_events(user=self.request.user):
            queryset = queryset | EventFile.objects.filter(event=event, visibility=EventFile.FileVisibility.SUBSCRIBED)

        return queryset

    def create(self, request, *args, **kwargs):
        # ToDo: check if file was uploaded to filemgr
        event = get_object_or_404(Event.objects.all(), id=self.kwargs['event_id'])
        request.data['event'] = str(event.id)

        filemgr_uuid = request.data['filemgr_uuid'] if 'filemgr_uuid' in request.data else False
        auth_token = get_authorization_header(request).split()[1].decode()
        if filemgr_uuid and not filemgr_service.check_file_id_exists(request.data['filemgr_uuid'], auth_token):
            raise NotFoundException('The file does not exists.')

        return super(EventFileViewSet, self).create(request=request, *args, **kwargs)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        # ToDo: remove file from filemgr
        return super(EventFileViewSet, self).destroy(request=request, *args, **kwargs)
