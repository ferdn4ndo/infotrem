from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from infotrem.models.location_model import Location, LocationTrackGauge, LocationInformation
from infotrem.serializers.location_serializer import LocationSerializer, LocationTrackGaugeSerializer, \
    LocationInformationSerializer
from infotrem.services.policy import IsLoggedIn, IsModeratorOrReadOnly


class LocationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationSerializer(location)
        return serializer.data

    def partial_update(self, request, pk=None):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationSerializer(location, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)


class LocationTrackGaugeViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, location_id=None):
        location = get_object_or_404(Location.objects.all(), pk=location_id)
        queryset = LocationTrackGauge.objects.filter(location=location)
        serializer = LocationTrackGaugeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, location_id=None):
        data = request.data
        data['location_id'] = location_id
        serializer = LocationTrackGaugeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, location_id=None, pk=None):
        location = get_object_or_404(Location.objects.all(), pk=location_id)
        queryset = LocationTrackGauge.objects.filter(location=location)
        track_gauge = get_object_or_404(queryset, pk=pk)
        serializer = LocationTrackGaugeSerializer(track_gauge)
        return Response(serializer.data)

    def partial_update(self, request, location_id=None, pk=None):
        location = get_object_or_404(Location.objects.all(), pk=location_id)
        queryset = LocationTrackGauge.objects.filter(location=location)
        track_gauge = get_object_or_404(queryset, pk=pk)
        serializer = LocationTrackGaugeSerializer(track_gauge)
        return Response(serializer.data)

    def destroy(self, request, location_id=None, pk=None):
        location = get_object_or_404(Location.objects.all(), pk=location_id)
        queryset = LocationTrackGauge.objects.filter(location=location)
        track_gauge = get_object_or_404(queryset, pk=pk)
        serializer = LocationTrackGaugeSerializer(track_gauge)
        return Response(serializer.data)


class LocationInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, location_id=None):
        location = get_object_or_404(Location.objects.all(), pk=location_id)
        queryset = LocationInformation.objects.filter(location=location)
        serializer = LocationInformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, location_id=None):
        data = request.data
        data['location_id'] = location_id
        serializer = LocationInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, location_id=None, pk=None):
        location = get_object_or_404(Location.objects.all(), pk=location_id)
        queryset = LocationInformation.objects.filter(location=location)
        information = get_object_or_404(queryset, pk=pk)
        serializer = LocationInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, location_id=None, pk=None):
        location = get_object_or_404(Location.objects.all(), pk=location_id)
        queryset = LocationInformation.objects.filter(location=location)
        information = get_object_or_404(queryset, pk=pk)
        serializer = LocationInformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, location_id=None, pk=None):
        location = get_object_or_404(Location.objects.all(), pk=location_id)
        queryset = LocationInformation.objects.filter(location=location)
        information = get_object_or_404(queryset, pk=pk)
        serializer = LocationInformationSerializer(information)
        return Response(serializer.data)
