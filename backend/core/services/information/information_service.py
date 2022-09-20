from typing import Dict

from core.services.information.information_effect_service import InformationEffectService
from core.models import Information


class InformationService:

    @staticmethod
    def create_information_from_data(information_data: Dict, created_by: str) -> Information:
        effects_data = information_data.pop('effects')
        information_data['created_by'] = created_by

        information = Information()
        information.update_from_dict(input_data=information_data)
        information.save()

        InformationEffectService.create_effects_from_data(
            effects_data=effects_data,
            information=information,
            created_by=created_by,
        )

        return information

    @staticmethod
    def update_information_from_data(information_data: Dict, information: Information, updated_by: str) -> Information:
        effects_data = information_data.pop('effects')
        information_data['updated_by'] = updated_by

        information.update_from_dict(input_data=information_data)
        information.save()

        InformationEffectService.update_effects_from_data(
            effects_data=effects_data,
            information=information,
            updated_by=updated_by,
        )

        return information
