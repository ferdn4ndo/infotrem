from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.models import Subscription, get_object_or_404, SubscriptionBillet
from api.serializers import EventFileSerializer
from api.services import policy


class SubscriptionBilletDownloadViewSet(ViewSet):
    permission_classes = [policy.IsLoggedIn]
    serializer_class = EventFileSerializer

    def list(self, request: Request):
        user = request.user
        subscription = get_object_or_404(Subscription.get_queryset_from_user(user), id=self.kwargs['subscription_id'])
        subscription_billet = get_object_or_404(
            SubscriptionBillet.objects.filter(subscription=subscription),
            id=self.kwargs['billet_id']
        )
        response = {"url": subscription_billet.billet.generate_download_link()}
        return Response(response, status.HTTP_200_OK)

