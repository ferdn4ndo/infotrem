from rest_framework import serializers

from api.models import LocationInformation, Location
from api.models.information_model import Information
from api.serializers.information_serializer import InformationSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer


class LocationInformationSerializer(GenericAuditedModelSerializer):
    location_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = LocationInformation
        fields = ['id', 'location_id', 'information']

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
