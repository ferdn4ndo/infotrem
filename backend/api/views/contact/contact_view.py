from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import api.policies.allow_all_policy
from api.serializers.contact.contact_serializer import ContactSerializer
from api.services import throttling
from core.services.mailer.mailer_service import MailerService


class ContactView(APIView):
    permission_classes = [api.policies.allow_all_policy.AllowAllPolicy]
    throttle_classes = (throttling.ContactRateThrottle,)

    @csrf_exempt
    def post(self, request, format=None):
        request.data['created_at'] = timezone.now()
        request.data['created_by'] = request.user.id if request.user is not None else None
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()

        mailer = MailerService()
        mailer.send_from_contact(contact)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
