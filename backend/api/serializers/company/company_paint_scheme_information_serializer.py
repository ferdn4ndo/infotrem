from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_serializer import InformationSerializer
from core.models import CompanyPaintSchemeInformation, Information, CompanyPaintScheme


class CompanyPaintSchemeInformationSerializer(GenericAuditedModelSerializer):
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
