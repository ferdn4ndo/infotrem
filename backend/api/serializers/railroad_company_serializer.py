from rest_framework import serializers

from api.serializers.information.information_serializer import InformationSerializer
from core.models.company.company_information_model import CompanyInformation
from core.models.company.company_model import Company
from core.models.company.company_paint_scheme_information_model import CompanyPaintSchemeInformation
from core.models.company.company_paint_scheme_model import CompanyPaintScheme
from core.models.information.information_model import Information


class CompanyInformationSerializer(serializers.ModelSerializer):
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


class CompanySerializer(serializers.ModelSerializer):
    company_information = CompanyInformationSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'abbrev', 'name', 'company_information']


class CompanyPaintSchemeInformationSerializer(serializers.ModelSerializer):
    paint_scheme_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = CompanyPaintSchemeInformation
        fields = ['id', 'paint_scheme_id', 'information']

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        paint_scheme = CompanyPaintScheme.objects.get(id=validated_data['paint_scheme_id'])
        return CompanyPaintSchemeInformation.objects.create(paint_scheme=paint_scheme, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance


class CompanyPaintSchemeSerializer(serializers.ModelSerializer):
    railroad = CompanySerializer()
    railroad_information = CompanyPaintSchemeInformationSerializer(many=True)

    class Meta:
        model = CompanyPaintScheme
        fields = ['id', 'name', 'railroad', 'start_date', 'end_date', 'railroad_information']
