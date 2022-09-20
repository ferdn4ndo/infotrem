from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models import RouteSectionLocationKilometer, RouteSectionLocation


class RouteSectionLocationKilometerSerializer(GenericAuditedModelSerializer):
    railroad_route_section_location_id = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = RouteSectionLocationKilometer
        fields = ['id', 'railroad_route_section_location_id', 'kilometer', 'kilometer_year', 'elevation']

    def create(self, validated_data):
        location = RouteSectionLocation.objects.get(id=validated_data.pop('railroad_route_section_location_id'))
        return RouteSectionLocationKilometer.objects.create(railroad_route_section_location=location, **validated_data)
