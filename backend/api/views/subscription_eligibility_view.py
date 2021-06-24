from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import get_object_or_404
from api.models.user_model import User
from api.models.event_vacancy_model import EventVacancy
from api.serializers.subscription_eligibility_serializer import SubscriptionEligibilitySerializer
from api.services.policy import IsLoggedIn
from api.services.subscription_eligibility import SubscriptionEligibility


class SubscriptionEligibilityView(APIView):
    permission_classes = [IsLoggedIn]

    def post(self, request, format=None):
        serializer = SubscriptionEligibilitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User.objects.all(), id=serializer.validated_data['candidate'])
        vacancy = get_object_or_404(EventVacancy.objects.all(), id=serializer.validated_data['vacancy'])
        subscription_service = SubscriptionEligibility(user=user, vacancy=vacancy)

        return Response(subscription_service.prepare_response_dict())
