from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models.manufacturer.manufacturer_model import Manufacturer


class ManufacturerSerializer(GenericAuditedModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'
