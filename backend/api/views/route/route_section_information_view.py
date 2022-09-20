from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers.route.route_section_information_serializer import RouteSectionInformationSerializer
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from core.models import Route, RouteSection, RouteSectionInformation


class RouteSectionInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]

    def list(self, request, route_id=None, section_id=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        section = get_object_or_404(RouteSection.objects.all(), pk=section_id)
        section_queryset = RouteSectionInformation.objects.filter(railroad_route_section=section)
        serializer = RouteSectionInformationSerializer(section_queryset, many=True)
        return Response(serializer.data)

    def create(self, request, route_id=None, section_id=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        section = get_object_or_404(RouteSection.objects.all(), pk=section_id)
        data = request.data
        data['railroad_route_section_id'] = section.id
        serializer = RouteSectionInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        section = get_object_or_404(RouteSection.objects.all(), pk=section_id)
        queryset = RouteSectionInformation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RouteSectionInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        section = get_object_or_404(RouteSection.objects.all(), pk=section_id)
        queryset = RouteSectionInformation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RouteSectionInformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, route_id=None, section_id=None, pk=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        section = get_object_or_404(RouteSection.objects.all(), pk=section_id)
        queryset = RouteSectionInformation.objects.filter(railroad_route_section=section)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RouteSectionInformationSerializer(information)
        return Response(serializer.data)
