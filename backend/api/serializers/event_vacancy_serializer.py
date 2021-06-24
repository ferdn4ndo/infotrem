from api.models import EventVacancy

from .event_vacancy_type_serializer import EventVacancyTypeSerializer
from .generic_audited_model_serializer import GenericAuditedModelSerializer


class EventVacancySerializer(GenericAuditedModelSerializer):
    type = EventVacancyTypeSerializer(allow_null=True)

    class Meta:
        model = EventVacancy
        fields = '__all__'
