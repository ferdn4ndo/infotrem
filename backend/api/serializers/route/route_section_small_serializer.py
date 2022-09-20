from api.serializers.company.company_serializer import CompanySerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.route.route_serializer import RouteSerializer
from core.models import RouteSection


class RouteSectionSmallSerializer(GenericAuditedModelSerializer):
    railroad_route = RouteSerializer()
    builder_railroad = CompanySerializer()

    class Meta:
        model = RouteSection
        fields = [
            'id',
            'railroad_route',
            'name',
            'builder_railroad',
            'build_year',
        ]
