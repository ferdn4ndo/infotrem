from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.route.route_section_location_kilometer_serializer import RouteSectionLocationKilometerSerializer
from core.models import RouteSectionLocation, Route, RouteSection, Location, RouteSectionLocationKilometer


class RouteSectionLocationSerializer(GenericAuditedModelSerializer):
    railroad_route_id = serializers.CharField(required=True, write_only=True)
    railroad_route_section_id = serializers.CharField(required=True, write_only=True)
    location_id = serializers.CharField(required=True, write_only=True)
    kilometers = RouteSectionLocationKilometerSerializer(many=True)

    class Meta:
        model = RouteSectionLocation
        fields = [
            'id',
            'railroad_route_id',
            'railroad_route_section_id',
            'location_id',
            'location_route_order',
            'kilometers',
        ]

    def create(self, validated_data):
        railroad_route = Route.objects.get(id=validated_data.pop('railroad_route_id'))
        railroad_route_section = RouteSection.objects.get(id=validated_data.pop('railroad_route_section_id'))
        location = Location.objects.get(id=validated_data.pop('location_id'))
        kilometers = validated_data.pop('kilometers')
        route_section_location = RouteSectionLocation.objects.create(
            railroad_route=railroad_route,
            railroad_route_section=railroad_route_section,
            location=location,
            **validated_data
        )
        for kilometer_data in kilometers:
            kilometer_data['railroad_route_section_location_id'] = route_section_location.id
            serializer = RouteSectionLocationKilometerSerializer(data=kilometer_data)
            serializer.save()
        return route_section_location

    def update(self, instance, validated_data):
        instance.railroad_route = Route.objects.get(id=validated_data.pop('railroad_route_id'))
        instance.railroad_route_section = RouteSection.objects.get(id=validated_data.pop('railroad_route_section_id'))
        instance.location = Location.objects.get(id=validated_data.pop('location_id'))

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        kilometers = validated_data.pop('kilometers')
        kilometers_dict = dict((i.id, i) for i in RouteSectionLocationKilometer.objects.filter(
            railroad_route_section_location=instance
        ))
        for kilometer_data in kilometers:
            if 'id' in kilometer_data and kilometer_data['id'] in kilometers_dict:
                kilometer = RouteSectionLocationKilometer.objects.get(id=kilometer_data['id'])
                kilometer_serializer = RouteSectionLocationKilometerSerializer(
                    instance=kilometer,
                    data=kilometer_data
                )
                kilometer_serializer.save()
            else:
                gauge_serializer = RouteSectionLocationKilometerSerializer(data=kilometer_data)
                gauge_serializer.save()
        if len(kilometers_dict) > 0:
            for item in kilometers_dict.values():
                item.delete()

        return instance
