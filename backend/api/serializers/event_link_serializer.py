from api.models import EventLink

from .generic_audited_model_serializer import GenericAuditedModelSerializer


class EventLinkSerializer(GenericAuditedModelSerializer):

    class Meta:
        model = EventLink
        fields = '__all__'
