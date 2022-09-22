from api.serializers.company.company_information_serializer import CompanyInformationSerializer
from api.serializers.company.company_paint_scheme_serializer import CompanyPaintSchemeSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models import Company


class CompanySerializer(GenericAuditedModelSerializer):
    company_information = CompanyInformationSerializer(many=True, read_only=True)
    company_paint_schemes = CompanyPaintSchemeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = [
            'id',
            'abbrev',
            'name',
            'company_information',
            'company_paint_schemes',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]
