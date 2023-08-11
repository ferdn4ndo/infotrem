from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_serializer import InformationSerializer
from core.models import RouteInformation, Information, Route


class RouteInformationSerializer(GenericAuditedModelSerializer):
    railroad_route_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = RouteInformation
        fields = ['id', 'railroad_route_id', 'information']

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        railroad_route = Route.objects.get(id=validated_data['railroad_route_id'])
        return RouteInformation.objects.create(railroad_route=railroad_route, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance