from api.models import EventVacancyType

from .generic_audited_model_serializer import GenericAuditedModelSerializer


class EventVacancyTypeSerializer(GenericAuditedModelSerializer):
    class Meta:
        model = EventVacancyType
        fields = '__all__'
