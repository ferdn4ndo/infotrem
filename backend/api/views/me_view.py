from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import MeSerializer
from api.services import policy


class MeView(APIView):
    permission_classes = [policy.IsLoggedIn]

    def get(self, request, format=None):
        serializer = MeSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request, format=None):
        request.data['updated_at'] = timezone.now()
        request.data['updated_by'] = request.user.id
        serializer = MeSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
