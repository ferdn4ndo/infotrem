from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers.route.route_section_serializer import RouteSectionSerializer
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from core.models import Route, RouteInformation, RouteSection


class RouteSectionViewSet(viewsets.ViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]

    def list(self, request, route_id=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        queryset = RouteInformation.objects.filter(railroad_route=route)
        serializer = RouteSectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, route_id=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        data = request.data
        data['railroad_route'] = route
        serializer = RouteSectionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, route_id=None, pk=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        queryset = RouteSection.objects.filter(railroad_route=route)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RouteSectionSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, route_id=None, pk=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        queryset = RouteSection.objects.filter(railroad_route=route)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RouteSectionSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, route_id=None, pk=None):
        route = get_object_or_404(Route.objects.all(), pk=route_id)
        queryset = RouteSection.objects.filter(railroad_route=route)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RouteSectionSerializer(information)
        return Response(serializer.data)
