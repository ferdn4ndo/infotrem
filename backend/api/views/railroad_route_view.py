from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from infotrem.models.railroad_route_model import RailroadRoute, RailroadRouteInformation, RailroadRouteSection, \
    RailroadRouteSectionInformation, RailroadRouteSectionLocation, RailroadRouteSectionPath
from infotrem.serializers.railroad_route_serializer import RailroadRouteSerializer, RailroadRouteInformationSerializer, \
    RailroadRouteSectionSerializer, RailroadRouteSectionInformationSerializer, RailroadRouteSectionLocationSerializer, \
    RailroadRouteSectionPathSerializer
from infotrem.services.policy import IsLoggedIn, IsModeratorOrReadOnly


class RailroadRouteViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request):
        queryset = RailroadRoute.objects.all()
        serializer = RailroadRouteSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = RailroadRoute.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSerializer(company)
        return serializer.data

    def partial_update(self, request, pk=None):
        queryset = RailroadRoute.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSerializer(company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = RailroadRoute.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSerializer(company)
        return Response(serializer.data)


class RailroadRouteInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, route_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        queryset = RailroadRouteInformation.objects.filter(railroad_route=route)
        serializer = RailroadRouteInformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, route_id=None):
        data = request.data
        data['railroad_route_id'] = route_id
        serializer = RailroadRouteInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, route_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        queryset = RailroadRouteInformation.objects.filter(railroad_route=route)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, route_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        queryset = RailroadRouteInformation.objects.filter(railroad_route=route)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteInformationSerializer(information)
        return Response(serializer.data)


class RailroadRouteSectionViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, route_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        queryset = RailroadRouteInformation.objects.filter(railroad_route=route)
        serializer = RailroadRouteSectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, route_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        data = request.data
        data['railroad_route'] = route
        serializer = RailroadRouteSectionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, route_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        queryset = RailroadRouteSection.objects.filter(railroad_route=route)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, route_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        queryset = RailroadRouteSection.objects.filter(railroad_route=route)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, route_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        queryset = RailroadRouteSection.objects.filter(railroad_route=route)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionSerializer(information)
        return Response(serializer.data)


class RailroadRouteSectionInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, route_id=None, section_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        section_queryset = RailroadRouteSectionInformation.objects.filter(railroad_route_section=section)
        serializer = RailroadRouteSectionInformationSerializer(section_queryset, many=True)
        return Response(serializer.data)

    def create(self, request, route_id=None, section_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        data = request.data
        data['railroad_route_section_id'] = section.id
        serializer = RailroadRouteSectionInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionInformation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionInformation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionInformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionInformation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionInformationSerializer(information)
        return Response(serializer.data)


class RailroadRouteSectionLocationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, route_id=None, section_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        section_queryset = RailroadRouteSectionLocation.objects.filter(railroad_route_section=section)
        serializer = RailroadRouteSectionLocationSerializer(section_queryset, many=True)
        return Response(serializer.data)

    def create(self, request, route_id=None, section_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        data = request.data
        data['railroad_route_section_id'] = section.id
        serializer = RailroadRouteSectionLocationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionLocation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionLocationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionLocation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionLocationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionLocation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionLocationSerializer(information)
        return Response(serializer.data)


class RailroadRouteSectionPathViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, route_id=None, section_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        section_queryset = RailroadRouteSectionPath.objects.filter(railroad_route_section=section)
        serializer = RailroadRouteSectionPathSerializer(section_queryset, many=True)
        return Response(serializer.data)

    def create(self, request, route_id=None, section_id=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        data = request.data
        data['railroad_route_section_id'] = section.id
        serializer = RailroadRouteSectionPathSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionPath.objects.filter(railroad_route_section=section)
        path = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionPathSerializer(path)
        return Response(serializer.data)

    def partial_update(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionPath.objects.filter(railroad_route_section=section)
        path = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionPathSerializer(path)
        return Response(serializer.data)

    def destroy(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(RailroadRoute.objects.all(), pk=route_id)
        section = get_object_or_404(RailroadRouteSection.objects.all(), pk=section_id)
        queryset = RailroadRouteSectionPath.objects.filter(railroad_route_section=section)
        path = get_object_or_404(queryset, pk=pk)
        serializer = RailroadRouteSectionPathSerializer(path)
        return Response(serializer.data)
