from rest_framework import serializers

from api.serializers.information.information_serializer import InformationSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models.information.information_model import Information
from core.models.location.location_information_model import LocationInformation
from core.models.location.location_model import Location


class LocationInformationSerializer(GenericAuditedModelSerializer):
    location_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = LocationInformation
        fields = [
            'id',
            'location_id',
            'information',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        location = Location.objects.get(id=validated_data['location_id'])
        return LocationInformation.objects.create(location=location, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance
