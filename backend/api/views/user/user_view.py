import os

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.policies.is_admin_or_deny_policy import IsAdminOrDenyPolicy
from api.policies.is_logged_in_policy import IsLoggedInPolicy
from api.serializers.user.user_serializer import UserSerializer


class UserViewSet(ViewSet):
    permission_classes = [IsLoggedInPolicy, IsAdminOrDenyPolicy]

    def list(self, request: Request) -> Response:
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        data = request.data
        data['system_name'] = os.environ['USERVER_AUTH_SYSTEM_NAME']
        data['is_admin'] = False
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request: Request, pk: str) -> Response:
        queryset = User.objects.all()
        storage = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(storage)
        return Response(serializer.data, status.HTTP_200_OK)

    def partial_update(self, request: Request, pk: str) -> Response:
        queryset = User.objects.all()
        storage = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(storage, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request: Request, pk: str) -> Response:
        queryset = User.objects.all()
        storage = get_object_or_404(queryset, pk=pk)
        storage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
