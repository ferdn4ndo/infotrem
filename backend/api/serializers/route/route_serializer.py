from api.serializers.company.company_serializer import CompanySerializer
from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.route.route_information_serializer import RouteInformationSerializer
from core.models import Route


class RouteSerializer(GenericAuditedModelSerializer):
    builder_railroad = CompanySerializer()
    route_information = RouteInformationSerializer(many=True)

    class Meta:
        model = Route
        fields = ['id', 'name', 'builder_railroad', 'route_information']
