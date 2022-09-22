from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_serializer import InformationSerializer
from core.models import Company
from core.models.company.company_information_model import CompanyInformation
from core.services.company.company_information_service import CompanyInformationService


class CompanyInformationSerializer(GenericAuditedModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = CompanyInformation
        fields = [
            'id',
            'company_id',
            'information',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

    def create(self, validated_data):
        return CompanyInformationService.create_company_information_from_data(validated_data=validated_data)

    def update(self, instance, validated_data):
        return CompanyInformationService.update_company_information_from_data(
            validated_data=validated_data,
            company_information=instance,
        )
