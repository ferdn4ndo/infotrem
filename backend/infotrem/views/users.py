from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import authentication, permissions
from rest_framework import generics

from infotrem.serializers.user import UserSerializer


class AdminListUsers(generics.ListCreateAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


