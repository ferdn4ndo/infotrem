from typing import List

from django.utils import timezone

from api.serializers.information.information_effect_serializer import InformationEffectSerializer
from core.models import Information, InformationEffect


class InformationEffectService:
    information: Information

    def __init__(self, information: Information):
        self.information = information

    def create_effects_from_data(self, effects_data: List, user_id: str):
        for effect_data in effects_data:
            effect_data['information_id'] = str(self.information.id)
            effect_data['created_at'] = timezone.now()
            effect_data['created_by'] = user_id

            effect_serializer = InformationEffectSerializer(data=effect_data)
            effect_serializer.is_valid(raise_exception=True)
            effect_serializer.save()

    def update_effects_from_data(self, effects_data: List, user_id: str):
        existing_effects = InformationEffect.objects.filter(information=self.information)
        for existing_effect in existing_effects:
            existing_effect.delete()

        self.create_effects_from_request(effects_data=effects_data, user_id=user_id)
