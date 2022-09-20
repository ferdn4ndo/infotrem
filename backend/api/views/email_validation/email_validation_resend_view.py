from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView

import api.policies.is_logged_in_policy
from api.services import throttling
from core.services.email_validation.email_validation_service import EmailValidationService
from api.services.translation import Messages


class EmailValidationResendView(APIView):
    permission_classes = [api.policies.is_logged_in_policy.IsLoggedInPolicy]
    throttle_classes = (throttling.EmailValidationRateThrottle,)

    @csrf_exempt
    def post(self, request):
        validation_service = EmailValidationService(user=request.user)
        email_sent = validation_service.send_new_validation_mail()

        if not email_sent:
            return JsonResponse(
                {'message': Messages.MSG_EMAIL_ALREADY_VALIDATED},
                status=status.HTTP_409_CONFLICT
            )

        return JsonResponse(
            {'message': Messages.MSG_EMAIL_VALIDATION_HASH_SENT},
            status=status.HTTP_201_CREATED
        )
