from api.models import Subscription
from .event_vacancy_serializer import EventVacancySerializer
from .user_serializer import UserSerializer
from .generic_audited_model_serializer import GenericAuditedModelSerializer


class SubscriptionSerializer(GenericAuditedModelSerializer):
    candidate = UserSerializer()
    vacancy = EventVacancySerializer()

    class Meta:
        model = Subscription
        fields = '__all__'
