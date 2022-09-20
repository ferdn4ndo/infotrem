from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_serializer import InformationSerializer
from core.models.company.company_information_model import CompanyInformation
from core.models.company.company_model import Company
from core.models.information.information_model import Information


class CompanyInformationSerializer(GenericAuditedModelSerializer):
    railroad_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = CompanyInformation
        fields = ['id', 'railroad_id', 'information']

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        railroad = Company.objects.get(id=validated_data['railroad_id'])
        return CompanyInformation.objects.create(railroad=railroad, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance
