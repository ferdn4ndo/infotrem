from rest_framework import serializers

from infotrem.models.information_model import Information
from infotrem.models.location_model import Location
from infotrem.models.railroad_route_model import RailroadRouteInformation, RailroadRoute, \
    RailroadRouteSectionInformation, RailroadRouteSectionLocationKilometer, RailroadRouteSectionLocation, \
    RailroadRouteSection, RailroadRouteSectionPathPoint, RailroadRouteSectionPath
from infotrem.serializers.information_serializer import InformationSerializer
from infotrem.serializers.railroad_company_serializer import RailroadCompanySerializer


class RailroadRouteInformationSerializer(serializers.ModelSerializer):
    railroad_route_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = RailroadRouteInformation
        fields = ['id', 'railroad_route_id', 'information']

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        railroad_route = RailroadRoute.objects.get(id=validated_data['railroad_route_id'])
        return RailroadRouteInformation.objects.create(railroad_route=railroad_route, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance


class RailroadRouteSerializer(serializers.ModelSerializer):
    builder_railroad = RailroadCompanySerializer()
    route_information = RailroadRouteInformationSerializer(many=True)

    class Meta:
        model = RailroadRoute
        fields = ['id', 'name', 'builder_railroad', 'route_information']


class RailroadRouteSectionInformationSerializer(serializers.ModelSerializer):
    railroad_route_section_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = RailroadRouteSectionInformation
        fields = ['id', 'railroad_route_section_id', 'information']

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        railroad_route_section = RailroadRoute.objects.get(id=validated_data['railroad_route_section_id'])
        return RailroadRouteInformation.objects.create(railroad_route_section=railroad_route_section, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance


class RailroadRouteSectionLocationKilometerSerializer(serializers.ModelSerializer):
    railroad_route_section_location_id = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = RailroadRouteSectionLocationKilometer
        fields = ['id', 'railroad_route_section_location_id', 'kilometer', 'kilometer_year', 'elevation']

    def create(self, validated_data):
        location = RailroadRouteSectionLocation.objects.get(id=validated_data.pop('railroad_route_section_location_id'))
        return RailroadRouteSectionLocationKilometer.objects.create(railroad_route_section_location=location, **validated_data)


class RailroadRouteSectionLocationSerializer(serializers.ModelSerializer):
    railroad_route_id = serializers.CharField(required=True, write_only=True)
    railroad_route_section_id = serializers.CharField(required=True, write_only=True)
    location_id = serializers.CharField(required=True, write_only=True)
    kilometers = RailroadRouteSectionLocationKilometerSerializer(many=True)

    class Meta:
        model = RailroadRouteSectionLocation
        fields = [
            'id',
            'railroad_route_id',
            'railroad_route_section_id',
            'location_id',
            'location_route_order',
            'kilometers',
        ]

    def create(self, validated_data):
        railroad_route = RailroadRoute.objects.get(id=validated_data.pop('railroad_route_id'))
        railroad_route_section = RailroadRouteSection.objects.get(id=validated_data.pop('railroad_route_section_id'))
        location = Location.objects.get(id=validated_data.pop('location_id'))
        kilometers = validated_data.pop('kilometers')
        route_section_location = RailroadRouteSectionLocation.objects.create(
            railroad_route=railroad_route,
            railroad_route_section=railroad_route_section,
            location=location,
            **validated_data
        )
        for kilometer_data in kilometers:
            kilometer_data['railroad_route_section_location_id'] = route_section_location.id
            serializer = RailroadRouteSectionLocationKilometerSerializer(data=kilometer_data)
            serializer.save()
        return route_section_location

    def update(self, instance, validated_data):
        instance.railroad_route = RailroadRoute.objects.get(id=validated_data.pop('railroad_route_id'))
        instance.railroad_route_section = RailroadRouteSection.objects.get(id=validated_data.pop('railroad_route_section_id'))
        instance.location = Location.objects.get(id=validated_data.pop('location_id'))

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        kilometers = validated_data.pop('kilometers')
        kilometers_dict = dict((i.id, i) for i in RailroadRouteSectionLocationKilometer.objects.filter(
            railroad_route_section_location=instance
        ))
        for kilometer_data in kilometers:
            if 'id' in kilometer_data and kilometer_data['id'] in kilometers_dict:
                kilometer = RailroadRouteSectionLocationKilometer.objects.get(id=kilometer_data['id'])
                kilometer_serializer = RailroadRouteSectionLocationKilometerSerializer(
                    instance=kilometer,
                    data=kilometer_data
                )
                kilometer_serializer.save()
            else:
                gauge_serializer = RailroadRouteSectionLocationKilometerSerializer(data=kilometer_data)
                gauge_serializer.save()
        if len(kilometers_dict) > 0:
            for item in kilometers_dict.values():
                item.delete()

        return instance


class RailroadRouteSectionPathPointSerializer(serializers.ModelSerializer):
    railroad_route_section_path_id = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = RailroadRouteSectionPathPoint
        fields = ['id', 'railroad_route_section_path_id', 'latitude', 'longitude', 'elevation']

    def create(self, validated_data):
        path = RailroadRouteSectionPath.objects.get(id=validated_data.pop('railroad_route_section_path_id'))
        return RailroadRouteSectionLocationKilometer.objects.create(railroad_route_section_path=path, **validated_data)


class RailroadRouteSectionPathSerializer(serializers.ModelSerializer):
    railroad_route_id = serializers.CharField(required=True, write_only=True)
    railroad_route_section_id = serializers.CharField(required=True, write_only=True)
    points = RailroadRouteSectionPathPointSerializer(many=True)

    class Meta:
        model = RailroadRouteSectionPath
        fields = [
            'id',
            'railroad_route_id',
            'railroad_route_section_id',
            'name',
            'points',
        ]

    def create(self, validated_data):
        railroad_route = RailroadRoute.objects.get(id=validated_data.pop('railroad_route_id'))
        railroad_route_section = RailroadRouteSection.objects.get(id=validated_data.pop('railroad_route_section_id'))
        points = validated_data.pop('points')
        route_section_path = RailroadRouteSectionPath.objects.create(
            railroad_route=railroad_route,
            railroad_route_section=railroad_route_section,
            **validated_data
        )
        for point_data in points:
            point_data['railroad_route_section_path_id'] = route_section_path.id
            serializer = RailroadRouteSectionPathPointSerializer(data=point_data)
            serializer.save()
        return route_section_path

    def update(self, instance, validated_data):
        instance.railroad_route = RailroadRoute.objects.get(id=validated_data.pop('railroad_route_id'))
        instance.railroad_route_section = RailroadRouteSection.objects.get(id=validated_data.pop('railroad_route_section_id'))

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        points = validated_data.pop('points')
        points_dict = dict((i.id, i) for i in RailroadRouteSectionPathPoint.objects.filter(
            railroad_route_section_path=instance
        ))
        for point_data in points:
            if 'id' in point_data and point_data['id'] in points_dict:
                point = RailroadRouteSectionPathPoint.objects.get(id=point_data['id'])
                point_serializer = RailroadRouteSectionPathPointSerializer(
                    instance=point,
                    data=point_data
                )
                point_serializer.save()
            else:
                gauge_serializer = RailroadRouteSectionPathPointSerializer(data=point_data)
                gauge_serializer.save()
        if len(points_dict) > 0:
            for item in points_dict.values():
                item.delete()

        return instance


class RailroadRouteSectionSerializer(serializers.ModelSerializer):
    railroad_route = RailroadRouteSerializer()
    builder_railroad = RailroadCompanySerializer()
    section_locations = RailroadRouteSectionLocationSerializer(many=True, read_only=True)

    class Meta:
        model = RailroadRouteSection
        fields = [
            'id',
            'railroad_route',
            'name',
            'builder_railroad',
            'build_year',
            'section_locations',
        ]

    def create(self, validated_data):
        railroad_route_data = validated_data.pop('railroad_route')
        railroad_route = RailroadRoute.objects.get(id=railroad_route_data['id'])

        builder_railroad_data = validated_data.pop('builder_railroad')
        builder_railroad = RailroadRoute.objects.get(id=builder_railroad_data['id'])

        route_section_location = RailroadRouteSection.objects.create(
            railroad_route=railroad_route,
            builder_railroad=builder_railroad,
            **validated_data
        )

        return route_section_location

    def update(self, instance, validated_data):
        railroad_route_data = validated_data.pop('railroad_route')
        instance.railroad_route = RailroadRoute.objects.get(id=railroad_route_data['id'])

        builder_railroad_data = validated_data.pop('builder_railroad')
        instance.builder_railroad = RailroadRoute.objects.get(id=builder_railroad_data['id'])

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        return instance
