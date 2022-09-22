from rest_framework import serializers

from api.serializers.company.company_paint_scheme_information_serializer import CompanyPaintSchemeInformationSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models import Company
from core.models.company.company_paint_scheme_model import CompanyPaintScheme
from core.services.company.company_paint_scheme_service import CompanyPaintSchemeService


class CompanyPaintSchemeSerializer(GenericAuditedModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        required=True,
        write_only=True,
    )
    company_paint_schemes_information = CompanyPaintSchemeInformationSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyPaintScheme
        fields = [
            'id',
            'name',
            'company_id',
            'company_paint_schemes_information',
            'start_date',
            'end_date',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

    def create(self, validated_data):
        return CompanyPaintSchemeService.create_company_paint_scheme_from_data(validated_data=validated_data)

    def update(self, instance, validated_data):
        return CompanyPaintSchemeService.update_company_paint_scheme_from_data(
            validated_data=validated_data,
            company_paint_scheme=instance,
        )
