from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models.contact.contact_model import Contact


class ContactSerializer(GenericAuditedModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
