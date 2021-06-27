from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.serializers.login_serializer import LoginSerializer
from api.services import auth, policy, throttling


class LoginViewSet(ViewSet):
    permission_classes = [policy.AllowAll]
    throttle_classes = (throttling.UserLoginRateThrottle,)

    def create(self, request: Request):
        """
        Tries to perform a login
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email, password = serializer.validated_data['email'], serializer.validated_data['password']
        service = auth.UServerAuthentication()
        login_response = service.perform_login(email=email, password=password)
        return Response(login_response, status=status.HTTP_201_CREATED)
