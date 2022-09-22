from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

import api.throttling.user_login_rate_throttle
from api.errors.conflict_exception import ConflictException
from api.models import get_object_or_404
from api.policies.allow_all_policy import AllowAllPolicy
from api.serializers.register.register_serializer import RegisterSerializer
from core.models.location.location_city_model import LocationCity
from core.models.location.location_state_model import LocationState
from core.models.user.user_model import User
from core.services.auth.u_server_authentication_service import UServerAuthenticationService
from core.services.email_validation.email_validation_service import EmailValidationService
from core.services.logger.logger_service import get_logger
from core.services.translation.translation_service import Messages


class RegisterViewSet(ViewSet):
    permission_classes = [AllowAllPolicy]
    throttle_classes = (api.throttling.user_login_rate_throttle.UserLoginRateThrottle,)

    def create(self, request: Request):
        """
        Tries to perform a login
        """
        logger = get_logger(__name__)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if len(User.objects.filter(email=serializer.validated_data['email'])):
            logger.debug("User already registered with email {}".format(serializer.validated_data['email']))
            raise ConflictException(Messages.MSG_EMAIL_ALREADY_REGISTERED)

        service = UServerAuthenticationService()
        data = serializer.validated_data
        user = service.get_user_or_create(
            username=data['email'],
            password=data['password']
        )

        user.name = data['name'] if 'name' in data else None
        user.rg = data['rg'] if 'rg' in data else None
        user.cpf = data['cpf'] if 'cpf' in data else None
        user.birth_date = data['birth_date'] if 'birth_date' in data else None
        user.address = data['address'] if 'address' in data else None
        user.number = data['number'] if 'number' in data else None
        user.complement = data['complement'] if 'complement' in data else None
        user.zipcode = data['zipcode'] if 'zipcode' in data else None
        user.phone = data['phone'] if 'phone' in data else None

        state_id = data['state_id'] if 'state_id' in data else None
        user.state = get_object_or_404(LocationState.objects.all(), id=state_id) if state_id else None

        city_id = data['city_id'] if 'city_id' in data else None
        user.city = get_object_or_404(LocationCity.objects.all(), id=city_id) if user.state and city_id else None

        user.save()
        logger.debug("user {} saved".format(user.id))

        register_response = service.perform_registration(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        logger.debug("register_response: {}".format(register_response))

        validation_service = EmailValidationService(user=user)
        email_sent = validation_service.send_new_validation_mail()
        logger.debug("email_sent: {}".format(email_sent))

        login_response = service.perform_login(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        logger.debug("login_response: {}".format(login_response))

        login_response['user_id'] = user.id

        return Response(login_response, status=status.HTTP_201_CREATED)
