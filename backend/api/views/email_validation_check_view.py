from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView

from api.models import get_object_or_404
from api.services import policy, throttling
from api.services.email_validation_service import EmailValidationService
from api.services.translation import Messages
from core.models.user.user_model import User


class EmailValidationCheckView(APIView):
    permission_classes = [policy.AllowAll]
    throttle_classes = (throttling.EmailValidationRateThrottle,)

    @csrf_exempt
    def get(self, request, user_id: str, validation_hash: str):
        user = get_object_or_404(User.objects.all(), id=user_id)

        validation_service = EmailValidationService(user=user)
        validated = validation_service.validate_user_hash(validation_hash)

        if not validated:
            return JsonResponse(
                {'message': Messages.MSG_INVALID_EMAIL_VALIDATION_HASH},
                status=status.HTTP_403_FORBIDDEN
            )

        return JsonResponse(
            {'message': Messages.MSG_EMAIL_SUCCESSFULLY_VALIDATED},
            status=status.HTTP_200_OK
        )
