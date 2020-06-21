from rest_framework import serializers


class InformationSerializer(serializers.ModelSerializer):
    """Serializer for the Information model"""

    track_gauge = TrackGaugeConfigurationSerializer()

    class Meta:
        model = Location
        fields = '__all__'
