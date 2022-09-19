from typing import Dict

from api.serializers.information.information_serializer import InformationSerializer
from core.models import InformationVote, Information, User, get_object_or_error
from core.services.information.information_effect_service import InformationEffectService


class InformationService:
    information: Information

    def __init__(self, information: Information):
        self.information = information

    def has_user_voted(self, user: User) -> bool:
        return InformationVote.objects.filter(information=self.information, created_by=user).exists()

    @staticmethod
    def create_information_from_data(information_data: Dict, user: User) -> Information:
        if not user.is_staff and not user.is_admin:
            information_data['status'] = Information.InformationStatus.DISCUSSION

        # Check if author exists
        if 'author_id' in information_data:
            get_object_or_error(queryset=User.objects.all(), pk=information_data['author_id'])

        effects_data = information_data['effects'] if 'effects' in information_data else []
        information_data['effects'] = []

        information_serializer = InformationSerializer(data=information_data)
        information_serializer.is_valid(raise_exception=True)
        information = information_serializer.save()

        information_effect_service = InformationEffectService(information=information)
        information_effect_service.create_effects_from_data(effects_data=effects_data, user_id=user.id)

        return information
