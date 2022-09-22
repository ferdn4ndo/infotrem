from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

import api.throttling.user_login_rate_throttle
from api.policies.allow_all_policy import AllowAllPolicy
from api.serializers.login.login_serializer import LoginSerializer
from core.services.auth.u_server_authentication_service import UServerAuthenticationService


class LoginViewSet(ViewSet):
    permission_classes = [AllowAllPolicy]
    throttle_classes = (api.throttling.user_login_rate_throttle.UserLoginRateThrottle,)

    def create(self, request: Request):
        """
        Tries to perform a login
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email, password = serializer.validated_data['email'], serializer.validated_data['password']
        service = UServerAuthenticationService()
        login_response = service.perform_login(email=email, password=password)
        return Response(login_response, status=status.HTTP_201_CREATED)
