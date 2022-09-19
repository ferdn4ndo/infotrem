from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.track_gauge_serializer import TrackGaugeSerializer
from core.models.information.information_model import Information
from core.models.location.location_model import Location
from core.models.location.location_track_gauge_model import LocationTrackGauge
from core.models.track_gauge.track_gauge_model import TrackGauge


class LocationTrackGaugeSerializer(GenericAuditedModelSerializer):
    location_id = serializers.CharField(required=True, write_only=True)
    track_gauge = TrackGaugeSerializer()

    class Meta:
        model = LocationTrackGauge
        fields = [
            'id',
            'location_id',
            'track_gauge',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

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
