from rest_framework import serializers

from infotrem.models.location import Location, LocationTrackGauge


class LocationSerializer(serializers.ModelSerializer):
    """Serializer for the Location model"""

    class Meta:
        model = Location
        fields = '__all__'


class LocationTrackGaugeSerializer(serializers.ModelSerializer):
    """Serializer for the Location model"""

    class Meta:
        model = LocationTrackGauge
        fields = '__all__'
