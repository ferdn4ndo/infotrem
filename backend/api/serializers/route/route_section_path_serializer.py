from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.route.route_section_path_point_serializer import RouteSectionPathPointSerializer
from core.models import Path, Route, RouteSection, PathPoint


class RouteSectionPathSerializer(GenericAuditedModelSerializer):
    railroad_route_id = serializers.CharField(required=True, write_only=True)
    railroad_route_section_id = serializers.CharField(required=True, write_only=True)
    points = RouteSectionPathPointSerializer(many=True)

    class Meta:
        model = Path
        fields = [
            'id',
            'railroad_route_id',
            'railroad_route_section_id',
            'name',
            'points',
        ]

    def create(self, validated_data):
        railroad_route = Route.objects.get(id=validated_data.pop('railroad_route_id'))
        railroad_route_section = RouteSection.objects.get(id=validated_data.pop('railroad_route_section_id'))
        points = validated_data.pop('points')
        route_section_path = Path.objects.create(
            railroad_route=railroad_route,
            railroad_route_section=railroad_route_section,
            **validated_data
        )
        for point_data in points:
            point_data['railroad_route_section_path_id'] = route_section_path.id
            serializer = RouteSectionPathPointSerializer(data=point_data)
            serializer.save()
        return route_section_path

    def update(self, instance, validated_data):
        instance.railroad_route = Route.objects.get(id=validated_data.pop('railroad_route_id'))
        instance.railroad_route_section = RouteSection.objects.get(id=validated_data.pop('railroad_route_section_id'))

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        points = validated_data.pop('points')
        points_dict = dict((i.id, i) for i in PathPoint.objects.filter(
            railroad_route_section_path=instance
        ))
        for point_data in points:
            if 'id' in point_data and point_data['id'] in points_dict:
                point = PathPoint.objects.get(id=point_data['id'])
                point_serializer = RouteSectionPathPointSerializer(
                    instance=point,
                    data=point_data
                )
                point_serializer.save()
            else:
                gauge_serializer = RouteSectionPathPointSerializer(data=point_data)
                gauge_serializer.save()
        if len(points_dict) > 0:
            for item in points_dict.values():
                item.delete()

        return instance
