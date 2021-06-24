from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from api.models.subscription_model import Subscription
from api.models.event_vacancy_model import EventVacancy
from api.models.user_model import User
from api.serializers import SubscriptionSerializer
from api.services import policy
from api.services.translation import Messages
from api.services.subscription_eligibility import SubscriptionEligibility

from .generic_model_view import FullCRUDListModelViewSet


class SubscriptionViewSet(FullCRUDListModelViewSet):
    permission_classes = [policy.IsLoggedIn, policy.IsAdminOrReadOnly]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        if self.request.user.is_admin:
            return Subscription.objects.all()
        return Subscription.objects.filter(candidate=self.request.user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not request.user.is_admin and request.user.id != serializer.validated_data['candidate']:
            return Response({'message': Messages.MSG_NOT_ENOUGH_PERMS}, status=status.HTTP_403_FORBIDDEN)

        user = User.objects.get(pk=serializer.validated_data['candidate'])
        vacancy = EventVacancy.objects.get(pk=serializer.validated_data['vacancy'])
        subscription_service = SubscriptionEligibility(user=user, vacancy=vacancy)

        if not subscription_service.is_eligible():
            return Response({'message': Messages.MSG_SUBSCRIPTION_NOT_ELIGIBLE}, status=status.HTTP_409_CONFLICT)

        subscription = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request: Request, *args, **kwargs) -> Response:
        if not request.user.is_admin:
            return Response({'message': Messages.MSG_NOT_ENOUGH_PERMS}, status=status.HTTP_403_FORBIDDEN)
        return super(SubscriptionViewSet, self).update(request=request, *args, **kwargs)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        if not request.user.is_admin:
            return Response({'message': Messages.MSG_NOT_ENOUGH_PERMS}, status=status.HTTP_403_FORBIDDEN)
        return super(SubscriptionViewSet, self).destroy(request=request, *args, **kwargs)
