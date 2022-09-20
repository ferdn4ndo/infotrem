from api.serializers.company.company_serializer import CompanySerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.route.route_section_location_serializer import RouteSectionLocationSerializer
from api.serializers.route.route_serializer import RouteSerializer
from core.models import RouteSection, Route


class RouteSectionSerializer(GenericAuditedModelSerializer):
    railroad_route = RouteSerializer()
    builder_railroad = CompanySerializer()
    section_locations = RouteSectionLocationSerializer(many=True, read_only=True)

    class Meta:
        model = RouteSection
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
        railroad_route = Route.objects.get(id=railroad_route_data['id'])

        builder_railroad_data = validated_data.pop('builder_railroad')
        builder_railroad = Route.objects.get(id=builder_railroad_data['id'])

        route_section_location = RouteSection.objects.create(
            railroad_route=railroad_route,
            builder_railroad=builder_railroad,
            **validated_data
        )

        return route_section_location

    def update(self, instance, validated_data):
        railroad_route_data = validated_data.pop('railroad_route')
        instance.railroad_route = Route.objects.get(id=railroad_route_data['id'])

        builder_railroad_data = validated_data.pop('builder_railroad')
        instance.builder_railroad = Route.objects.get(id=builder_railroad_data['id'])

        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        return instance
