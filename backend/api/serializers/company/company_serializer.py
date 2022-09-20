from api.serializers.company.company_information_serializer import CompanyInformationSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models import Company


class CompanySerializer(GenericAuditedModelSerializer):
    company_information = CompanyInformationSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'abbrev', 'name', 'company_information']
