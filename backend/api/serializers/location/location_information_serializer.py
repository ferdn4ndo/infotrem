from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_serializer import InformationSerializer
from core.services.information.information_service import InformationService
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

        information = InformationService.create_information_from_data(
            information_data=information_data,
            created_by=validated_data['created_by'],
        )

        location = Location.objects.get(id=validated_data['location_id'])

        location_information = LocationInformation()
        location_information.location = location
        location_information.information = information
        location_information.created_by = validated_data['created_by']
        location_information.save()

        return location_information

    def update(self, instance: LocationInformation, validated_data):
        information_data = validated_data.pop('information')

        instance.information = InformationService.update_information_from_data(
            information_data=information_data,
            information=instance.information,
            updated_by=validated_data['updated_by'],
        )

        instance.updated_by = validated_data['updated_by']
        instance.save()

        return instance
