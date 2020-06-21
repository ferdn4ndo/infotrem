from rest_framework import serializers

from infotrem.models.location import TrackGaugeConfiguration, Location


class TrackGaugeConfigurationSerializer(serializers.ModelSerializer):
    """Serializer for the TrackGaugeConfiguration model"""

    class Meta:
        model = TrackGaugeConfiguration
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    """Serializer for the Location model"""

    track_gauge = TrackGaugeConfigurationSerializer()

    class Meta:
        model = Location
        fields = '__all__'
