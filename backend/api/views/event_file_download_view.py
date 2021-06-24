from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.models import EventFile, Event, Subscription, get_object_or_404
from api.serializers import EventFileSerializer
from api.services import policy


class EventFileDownloadViewSet(ViewSet):
    permission_classes = [policy.IsLoggedIn]
    serializer_class = EventFileSerializer

    def list(self, request: Request):
        event = get_object_or_404(Event.objects.all(), id=self.kwargs['event_id'])
        user_subscribed_events = Subscription.get_user_subscribed_events(user=request.user)
        queryset = EventFile.objects.filter(event=event, visibility=EventFile.FileVisibility.EVERYONE)
        if event in user_subscribed_events:
            queryset = queryset | EventFile.objects.filter(event=event, visibility=EventFile.FileVisibility.SUBSCRIBED)
        file = get_object_or_404(queryset, id=self.kwargs['file_id'])
        response = {"url": file.generate_download_link()}
        return Response(response, status.HTTP_200_OK)
