from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.contact.contact_serializer import ContactSerializer
from api.services import policy, throttling
from api.services.mailer import Mailer


class ContactView(APIView):
    permission_classes = [policy.AllowAll]
    throttle_classes = (throttling.ContactRateThrottle,)

    @csrf_exempt
    def post(self, request, format=None):
        request.data['created_at'] = timezone.now()
        request.data['created_by'] = request.user.id if request.user is not None else None
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()

        mailer = Mailer()
        mailer.send_from_contact(contact)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
