from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_serializer import InformationSerializer
from core.models import CompanyPaintSchemeInformation, Information, CompanyPaintScheme
from core.services.company.company_paint_scheme_information_service import CompanyPaintSchemeInformationService


class CompanyPaintSchemeInformationSerializer(GenericAuditedModelSerializer):
    paint_scheme_id = serializers.PrimaryKeyRelatedField(
        queryset=CompanyPaintScheme.objects.all(),
        required=True,
        write_only=True,
    )
    information = InformationSerializer()

    class Meta:
        model = CompanyPaintSchemeInformation
        fields = [
            'id',
            'paint_scheme_id',
            'information',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

    def create(self, validated_data):
        return CompanyPaintSchemeInformationService.create_company_paint_scheme_information_from_data(
            validated_data=validated_data,
        )

    def update(self, instance, validated_data):
        return CompanyPaintSchemeInformationService.update_company_paint_scheme_information_from_data(
            validated_data=validated_data,
            company_paint_scheme_information=instance,
        )
