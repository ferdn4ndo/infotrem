from typing import List

from core.models import Information, InformationEffect


class InformationEffectService:

    @staticmethod
    def create_effects_from_data(effects_data: List, information: Information, created_by: str) -> InformationEffect:
        for effect_data in effects_data:
            effect = InformationEffect()
            effect.information = information
            effect.created_by = created_by
            effect.field_name=effect_data['field_name'],

            if 'old_value' in effect_data:
                effect.old_value=effect_data['old_value']

            if 'new_value' in effect_data:
                effect.new_value=effect_data['new_value']

            effect.save()

            return effect

    @staticmethod
    def update_effects_from_data(effects_data: List, information: Information, updated_by: str) -> InformationEffect:
        # We first delete the existing effects
        existing_effects = InformationEffect.objects.filter(information=information)
        for existing_effect in existing_effects:
            existing_effect.delete()

        # Then create the given ones
        return InformationEffectService.create_effects_from_data(
            effects_data=effects_data,
            information=information,
            created_by=updated_by,
        )
