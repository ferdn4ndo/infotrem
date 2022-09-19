from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_serializer import InformationSerializer
from core.models.information.information_model import Information
from core.models.manufacturer.manufacturer_information_model import ManufacturerInformation
from core.models.manufacturer.manufacturer_model import Manufacturer


class ManufacturerInformationSerializer(GenericAuditedModelSerializer):
    manufacturer_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = ManufacturerInformation
        fields = [
            'id',
            'manufacturer_id',
            'information',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        manufacturer = Manufacturer.objects.get(id=validated_data['manufacturer_id'])

        return ManufacturerInformation.objects.create(manufacturer=manufacturer, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])

        serializer = InformationSerializer(information, data=information_data)
        serializer.save()

        instance.information = information
        instance.save()

        return instance
