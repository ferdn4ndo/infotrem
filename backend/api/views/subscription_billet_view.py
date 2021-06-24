from django.db.models import QuerySet

from api.models import Billet, get_object_or_404, Subscription, SubscriptionBillet
from api.serializers import SubscriptionBilletSerializer
from api.services import policy
from .generic_model_view import ReadModelViewSet


class SubscriptionBilletViewSet(ReadModelViewSet):
    queryset = Billet.objects.all()
    serializer_class = SubscriptionBilletSerializer
    permission_classes = [policy.IsLoggedIn, policy.IsAdminOrDeny]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        subscription = get_object_or_404(Subscription.get_queryset_from_user(user), id=self.kwargs['subscription_id'])
        return SubscriptionBillet.objects.filter(subscription=subscription)
