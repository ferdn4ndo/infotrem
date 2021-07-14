from rest_framework import serializers

from api.models import LocationInformation, Location, LocationTrackGauge, RouteSectionLocation
from api.models.information_model import Information
from api.models.track_gauge_model import TrackGauge
from api.serializers.information_serializer import InformationSerializer
from api.serializers.railroad_route_serializer import RouteSerializer, RouteSectionSmallSerializer, \
    RouteSectionLocationKilometerSerializer, RouteSectionLocationSerializer
from api.serializers.track_gauge_serializer import TrackGaugeSerializer


class LocationInformationSerializer(serializers.ModelSerializer):
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


class LocationTrackGaugeSerializer(serializers.ModelSerializer):
    location_id = serializers.CharField(required=True, write_only=True)
    track_gauge = TrackGaugeSerializer()

    class Meta:
        model = LocationTrackGauge
        fields = ['id', 'location_id', 'track_gauge']

    def create(self, validated_data):
        gauge_data = validated_data.pop('track_gauge')
        gauge = TrackGauge.objects.get(tag=gauge_data['tag'])
        location = Location.objects.get(id=validated_data['location_id'])
        return LocationTrackGauge.objects.create(location=location, track_gauge=gauge)

    def update(self, instance, validated_data):
        gauge_data = validated_data.pop('track_gauge')
        gauge = Information.objects.get(id=gauge_data['id'])
        instance.track_gauge = gauge
        instance.save()
        return instance


class LocationRailroadRouteSectionSerializer(serializers.ModelSerializer):
    railroad_route = RouteSerializer()
    railroad_route_section = RouteSectionSmallSerializer()
    kilometers = RouteSectionLocationKilometerSerializer(many=True)

    class Meta:
        model = RouteSectionLocation
        fields = [
            'id',
            'railroad_route',
            'railroad_route_section',
            'location_route_order',
            'kilometers',
        ]


class LocationSerializer(serializers.ModelSerializer):
    information = LocationInformationSerializer(many=True)
    gauges = LocationTrackGaugeSerializer(many=True)
    route_sections = LocationRailroadRouteSectionSerializer(many=True, read_only=True)

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
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
            'information',
            'gauges',
            'route_sections',
        ]

    def create(self, validated_data):
        information = validated_data.pop('information')
        gauges = validated_data.pop('gauges')
        location = Location.objects.create(**validated_data)
        for gauge_data in gauges:
            serializer = LocationTrackGaugeSerializer(data=gauge_data)
            serializer.save()
        for information_data in information:
            serializer = LocationInformationSerializer(data=information_data)
            serializer.save()
        return location

    def update(self, instance, validated_data):
        information = validated_data.pop('information')
        gauges = validated_data.pop('gauges')
        route_sections = validated_data.pop('route_sections')

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        gauges_dict = dict((i.id, i) for i in LocationTrackGauge.objects.filter(location=instance))
        for gauge_data in gauges:
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
