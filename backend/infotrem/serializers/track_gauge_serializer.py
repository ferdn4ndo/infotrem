from rest_framework import serializers

from infotrem.models.track_gauge_model import TrackGauge


class TrackGaugeSerializer(serializers.ModelSerializer):
    """Serializer for the TrackGaugeSerializer model"""

    class Meta:
        model = TrackGauge
        fields = '__all__'
