from api.serializers.company.company_paint_scheme_information_serializer import CompanyPaintSchemeInformationSerializer
from api.serializers.company.company_serializer import CompanySerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models.company.company_paint_scheme_model import CompanyPaintScheme


class CompanyPaintSchemeSerializer(GenericAuditedModelSerializer):
    railroad = CompanySerializer()
    information = CompanyPaintSchemeInformationSerializer(many=True)

    class Meta:
        model = CompanyPaintScheme
        fields = [
            'id',
            'name',
            'railroad',
            'start_date',
            'end_date',
            'information',
        ]
