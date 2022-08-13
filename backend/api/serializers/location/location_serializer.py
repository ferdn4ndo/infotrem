from api.models import LocationInformation, Location, LocationTrackGauge, RouteSectionLocation
from api.serializers.railroad_route_serializer import RouteSectionLocationSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer

from .location_information_serializer import LocationInformationSerializer
from .location_railroad_route_section_serializer import LocationRailroadRouteSectionSerializer
from .location_track_gauge_serializer import LocationTrackGaugeSerializer


class LocationSerializer(GenericAuditedModelSerializer):
    information = LocationInformationSerializer(many=True)
    track_gauges = LocationTrackGaugeSerializer(many=True)
    route_sections = LocationRailroadRouteSectionSerializer(many=True)

    class Meta:
        model = Location
        fields = [
            'id',
            'abbrev',
            'name',
            'type',
            'status',
            'center_latitude',
            'center_longitude',
            'elevation',
            'city',
            'build_year',
            'other_names',
            'is_verified',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
            'information',
            'track_gauges',
            'route_sections',
        ]

    def create(self, validated_data):
        information = validated_data.pop('information')
        track_gauges = validated_data.pop('track_gauges')
        route_sections = validated_data.pop('route_sections')
        location = Location.objects.create(**validated_data)

        for gauge_data in track_gauges:
            serializer = LocationTrackGaugeSerializer(data=gauge_data)
            serializer.save()

        for information_data in information:
            serializer = LocationInformationSerializer(data=information_data)
            serializer.save()

        for route_section_data in route_sections:
            serializer = LocationRailroadRouteSectionSerializer(data=route_section_data)
            serializer.save()

        return location

    def update(self, instance, validated_data):
        information = validated_data.pop('information')
        track_gauges = validated_data.pop('track_gauges')
        route_sections = validated_data.pop('route_sections')

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        gauges_dict = dict((i.id, i) for i in LocationTrackGauge.objects.filter(location=instance))
        for gauge_data in track_gauges:
            if 'id' in gauge_data and gauge_data['id'] in gauges_dict:
                gauge = gauges_dict.pop(gauge_data['id'])
                gauge_data.pop('id')
                for key in gauge_data.keys():
                    setattr(gauge, key, gauge_data[key])
                gauge.save()
            else:
                gauge_serializer = LocationTrackGaugeSerializer(data=gauge_data)
                gauge_serializer.save()
        if len(gauges_dict) > 0:
            for item in gauges_dict.values():
                item.delete()

        information_dict = dict((i.id, i) for i in LocationInformation.objects.filter(location=instance))
        for information_data in information:
            if 'id' in information_data and information_data['id'] in information_dict:
                information = information_dict.pop(information_data['id'])
                information_data.pop('id')
                for key in information_data.keys():
                    setattr(information, key, information_data[key])
                information.save()
            else:
                information_serializer = LocationInformationSerializer(data=information_data)
                information_serializer.save()
        if len(information_dict) > 0:
            for item in information_dict.values():
                item.delete()

        route_sections_dict = dict((i.id, i) for i in RouteSectionLocation.objects.filter(location=instance))
        for section_data in route_sections:
            if 'id' in section_data and section_data['id'] in route_sections_dict:
                route_section = route_sections_dict.pop(section_data['id'])
                section_data.pop('id')
                for key in section_data.keys():
                    setattr(route_section, key, section_data[key])
                route_section.save()
            else:
                section_serializer = RouteSectionLocationSerializer(data=section_data)
                section_serializer.save()
        if len(route_sections_dict) > 0:
            for item in route_sections_dict.values():
                item.delete()

        return instance
