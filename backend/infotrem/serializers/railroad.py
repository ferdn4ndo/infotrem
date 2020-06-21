from rest_framework import serializers

from infotrem.models.railroad import RailroadCompany, Manufacturer, RailroadPaintScheme


class RailroadCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = RailroadCompany
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'


class RailroadPaintSchemeSerializer(serializers.ModelSerializer):
    railroad = RailroadCompanySerializer

    class Meta:
        model = RailroadPaintScheme
        fields = '__all__'
