from api.serializers.route.route_section_location_kilometer_serializer import RouteSectionLocationKilometerSerializer
from api.serializers.route.route_section_small_serializer import RouteSectionSmallSerializer
from api.serializers.route.route_serializer import RouteSerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models.route.route_section_location_model import RouteSectionLocation


class LocationRailroadRouteSectionSerializer(GenericAuditedModelSerializer):
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
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]
