from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.errors import ConflictException
from api.models import User, LocationState, get_object_or_404, LocationCity
from api.serializers import RegisterSerializer
from api.services import auth, policy, throttling, translation
from api.services.email_validation_service import EmailValidationService
from api.services.logger import get_logger


class RegisterViewSet(ViewSet):
    permission_classes = [policy.AllowAll]
    throttle_classes = (throttling.UserLoginRateThrottle,)

    def create(self, request: Request):
        """
        Tries to perform a login
        """
        logger = get_logger(__name__)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if len(User.objects.filter(email=serializer.validated_data['email'])):
            logger.debug("User already registered with email {}".format(serializer.validated_data['email']))
            raise ConflictException(translation.Messages.MSG_EMAIL_ALREADY_REGISTERED)

        service = auth.UServerAuthentication()
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

        user.relational_status = data['relational_status'] if 'relational_status' in data else None
        user.education_level_self = data['education_level_self'] if 'education_level_self' in data else None
        user.education_level_father = data['education_level_father'] if 'education_level_father' in data else None
        user.education_level_mother = data['education_level_mother'] if 'education_level_mother' in data else None
        user.has_children = data['has_children'] if 'has_children' in data else None
        user.total_children = data['total_children'] if 'total_children' in data else None
        user.youngest_child_birth_date = data['youngest_child_birth_date'] if 'youngest_child_birth_date' in data else None
        user.skin_color_or_racial_group = data['skin_color_or_racial_group'] if 'skin_color_or_racial_group' in data else None
        user.habitation_level = data['habitation_level'] if 'habitation_level' in data else None
        user.family_income_level = data['family_income_level'] if 'family_income_level' in data else None
        user.financial_status = data['financial_status'] if 'financial_status' in data else None
        user.job_status = data['job_status'] if 'job_status' in data else None
        
        user.special_needs = data['special_needs'] if 'special_needs' in data else None
        user.has_auditive_disability = data['has_auditive_disability'] if 'has_auditive_disability' in data else None
        user.has_physical_disability = data['has_physical_disability'] if 'has_physical_disability' in data else None
        user.has_mental_disability = data['has_mental_disability'] if 'has_mental_disability' in data else None
        user.has_motor_disability = data['has_motor_disability'] if 'has_motor_disability' in data else None
        user.has_visual_disability = data['has_visual_disability'] if 'has_visual_disability' in data else None
        user.has_other_disability = data['has_other_disability'] if 'has_other_disability' in data else None
        user.other_disability_detail = data['other_disability_detail'] if 'other_disability_detail' in data else None
        user.disease_id = data['disease_id'] if 'disease_id' in data else None
        user.doctor_name = data['doctor_name'] if 'doctor_name' in data else None
        user.needs_accommodation = data['needs_accommodation'] if 'needs_accommodation' in data else None
        user.needs_reader = data['needs_reader'] if 'needs_reader' in data else None
        user.needs_enlarged_exam = data['needs_enlarged_exam'] if 'needs_enlarged_exam' in data else None
        user.needs_typist = data['needs_typist'] if 'needs_typist' in data else None
        user.needs_other = data['needs_other'] if 'needs_other' in data else None
        user.other_needs_detail = data['other_needs_detail'] if 'other_needs_detail' in data else None

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
