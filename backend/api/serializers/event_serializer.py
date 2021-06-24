from api.models import Event

from .generic_audited_model_serializer import GenericAuditedModelSerializer
from .media_file_serializer import EventFileSerializer
from .event_link_serializer import EventLinkSerializer
from .event_vacancy_serializer import EventVacancySerializer


class EventSerializer(GenericAuditedModelSerializer):
    files = EventFileSerializer(many=True, required=False)
    links = EventLinkSerializer(many=True, required=False)
    vacancies = EventVacancySerializer(many=True, required=False)

    class Meta:
        model = Event
        fields = '__all__'
        extra_fields = [
            'is_open_for_subscriptions',
            'files',
            'links',
            'vacancies',
        ]
