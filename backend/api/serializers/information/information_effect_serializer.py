from rest_framework import serializers


from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models.information.information_effect_model import InformationEffect


class InformationEffectSerializer(GenericAuditedModelSerializer):
    information_id = serializers.CharField(required=False, write_only=True)
    field_name = serializers.CharField(required=True, allow_blank=False)
    old_value = serializers.CharField(required=False, allow_blank=True)
    new_value = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = InformationEffect
        fields = [
            'id',
            'information_id',
            'field_name',
            'old_value',
            'new_value',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]
