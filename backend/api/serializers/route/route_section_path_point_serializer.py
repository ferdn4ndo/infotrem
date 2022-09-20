from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models import PathPoint, Path, RouteSectionLocationKilometer


class RouteSectionPathPointSerializer(GenericAuditedModelSerializer):
    railroad_route_section_path_id = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = PathPoint
        fields = ['id', 'railroad_route_section_path_id', 'latitude', 'longitude', 'elevation']

    def create(self, validated_data):
        path = Path.objects.get(id=validated_data.pop('railroad_route_section_path_id'))
        return RouteSectionLocationKilometer.objects.create(railroad_route_section_path=path, **validated_data)
