from api.models.information_effect_model import InformationEffect
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer


class InformationEffectSerializer(GenericAuditedModelSerializer):

    class Meta:
        model = InformationEffect
        fields = '__all__'
