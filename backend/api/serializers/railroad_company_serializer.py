from rest_framework import serializers

from api.models.information_model import Information
from api.models.company_model import RailroadCompanyInformation, RailroadCompanyPaintSchemeInformation, \
    RailroadCompanyPaintScheme
from api.models.route_model import Company
from api.serializers.information_serializer import InformationSerializer


class RailroadCompanyInformationSerializer(serializers.ModelSerializer):
    company_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = RailroadCompanyInformation
        fields = ['id', 'railroad_id', 'information']

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        railroad = Company.objects.get(id=validated_data['railroad_id'])
        return RailroadCompanyInformation.objects.create(railroad=railroad, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance


class RailroadCompanySerializer(serializers.ModelSerializer):
    company_information = RailroadCompanyInformationSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'abbrev', 'name', 'company_information']


class RailroadCompanyPaintSchemeInformationSerializer(serializers.ModelSerializer):
    paint_scheme_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = RailroadCompanyPaintSchemeInformation
        fields = ['id', 'paint_scheme_id', 'information']

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        paint_scheme = RailroadCompanyPaintScheme.objects.get(id=validated_data['paint_scheme_id'])
        return RailroadCompanyPaintSchemeInformation.objects.create(paint_scheme=paint_scheme, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance


class RailroadCompanyPaintSchemeSerializer(serializers.ModelSerializer):
    railroad = RailroadCompanySerializer()
    railroad_information = RailroadCompanyPaintSchemeInformationSerializer(many=True)

    class Meta:
        model = RailroadCompanyPaintScheme
        fields = ['id', 'name', 'railroad', 'start_date', 'end_date', 'railroad_information']
