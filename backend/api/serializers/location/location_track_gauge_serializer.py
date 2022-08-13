from rest_framework import serializers

from api.models import Location, LocationTrackGauge
from api.models.information_model import Information
from api.models.track_gauge_model import TrackGauge
from api.serializers.track_gauge_serializer import TrackGaugeSerializer


class LocationTrackGaugeSerializer(serializers.ModelSerializer):
    location_id = serializers.CharField(required=True, write_only=True)
    track_gauge = TrackGaugeSerializer()

    class Meta:
        model = LocationTrackGauge
        fields = ['id', 'location_id', 'track_gauge']

    def create(self, validated_data):
        gauge_data = validated_data.pop('track_gauge')
        gauge = TrackGauge.objects.get(tag=gauge_data['tag'])
        location = Location.objects.get(id=validated_data['location_id'])
        return LocationTrackGauge.objects.create(location=location, track_gauge=gauge)

    def update(self, instance, validated_data):
        gauge_data = validated_data.pop('track_gauge')
        gauge = Information.objects.get(id=gauge_data['id'])
        instance.track_gauge = gauge
        instance.save()
        return instance
