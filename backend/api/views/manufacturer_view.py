from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from infotrem.models.manufacturer_model import ManufacturerInformation, Manufacturer
from infotrem.serializers.manufacturer_serializer import ManufacturerInformationSerializer, ManufacturerSerializer
from infotrem.services.policy import IsLoggedIn, IsModeratorOrReadOnly


class ManufacturerViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request):
        queryset = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = Manufacturer.objects.all()
        manufacturer = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerSerializer(manufacturer)
        return serializer.data

    def partial_update(self, request, pk=None):
        queryset = Manufacturer.objects.all()
        manufacturer = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerSerializer(manufacturer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Manufacturer.objects.all()
        manufacturer = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)


class ManufacturerInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, manufacturer_id=None):
        manufacturer = get_object_or_404(Manufacturer.objects.all(), pk=manufacturer_id)
        queryset = ManufacturerInformation.objects.filter(manufacturer=manufacturer)
        serializer = ManufacturerInformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, manufacturer_id=None):
        data = request.data
        data['manufacturer_id'] = manufacturer_id
        serializer = ManufacturerInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, manufacturer_id=None, pk=None):
        manufacturer = get_object_or_404(Manufacturer.objects.all(), pk=manufacturer_id)
        queryset = ManufacturerInformation.objects.filter(manufacturer=manufacturer)
        information = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, manufacturer_id=None, pk=None):
        manufacturer = get_object_or_404(Manufacturer.objects.all(), pk=manufacturer_id)
        queryset = ManufacturerInformation.objects.filter(manufacturer=manufacturer)
        information = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerInformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, manufacturer_id=None, pk=None):
        manufacturer = get_object_or_404(Manufacturer.objects.all(), pk=manufacturer_id)
        queryset = ManufacturerInformation.objects.filter(manufacturer=manufacturer)
        information = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerInformationSerializer(information)
        return Response(serializer.data)
