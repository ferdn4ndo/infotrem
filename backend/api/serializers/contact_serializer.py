from api.models import Contact
from .generic_audited_model_serializer import GenericAuditedModelSerializer


class ContactSerializer(GenericAuditedModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
