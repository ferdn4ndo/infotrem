from api.models import Holiday
from .generic_audited_model_serializer import GenericAuditedModelSerializer


class HolidaySerializer(GenericAuditedModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'
