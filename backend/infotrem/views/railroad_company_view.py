from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from infotrem.models.railroad_company_model import RailroadCompanyPaintScheme, RailroadCompanyPaintSchemeInformation, \
    RailroadCompany, RailroadCompanyInformation
from infotrem.serializers.railroad_company_serializer import RailroadCompanyPaintSchemeInformationSerializer, \
    RailroadCompanyPaintSchemeSerializer, RailroadCompanyInformationSerializer
from infotrem.serializers.railroad_route_serializer import RailroadCompanySerializer
from infotrem.services.policy import IsLoggedIn, IsModeratorOrReadOnly


class RailroadCompanyViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request):
        queryset = RailroadCompany.objects.all()
        serializer = RailroadCompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = RailroadCompany.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanySerializer(company)
        return serializer.data

    def partial_update(self, request, pk=None):
        queryset = RailroadCompany.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanySerializer(company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = RailroadCompany.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanySerializer(company)
        return Response(serializer.data)


class RailroadCompanyInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, company_id=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        queryset = RailroadCompanyInformation.objects.filter(company=company)
        serializer = RailroadCompanyInformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, company_id=None):
        data = request.data
        data['company_id'] = company_id
        serializer = RailroadCompanyInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, company_id=None, pk=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        queryset = RailroadCompanyInformation.objects.filter(company=company)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, company_id=None, pk=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        queryset = RailroadCompanyInformation.objects.filter(company=company)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyInformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, company_id=None, pk=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        queryset = RailroadCompanyInformation.objects.filter(company=company)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyInformationSerializer(information)
        return Response(serializer.data)


class RailroadCompanyPaintSchemeViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, company_id=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        queryset = RailroadCompanyPaintScheme.objects.filter(railroad=company)
        serializer = RailroadCompanyPaintSchemeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, company_id=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        queryset = RailroadCompanyPaintScheme.objects.filter(railroad=company)
        company = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyPaintSchemeSerializer(company)
        return serializer.data

    def partial_update(self, request, pk=None, company_id=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        queryset = RailroadCompanyPaintScheme.objects.filter(railroad=company)
        paint_scheme = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyPaintSchemeSerializer(paint_scheme, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None, company_id=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        queryset = RailroadCompanyPaintScheme.objects.filter(railroad=company)
        paint_scheme = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyPaintSchemeSerializer(paint_scheme)
        return Response(serializer.data)


class RailroadCompanyPaintSchemeInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsModeratorOrReadOnly]

    def list(self, request, company_id=None, paint_scheme_id=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(RailroadCompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        paint_scheme_queryset = RailroadCompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)
        serializer = RailroadCompanyPaintSchemeInformationSerializer(paint_scheme_queryset, many=True)
        return Response(serializer.data)

    def create(self, request, company_id=None, paint_scheme_id=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(RailroadCompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        data = request.data
        data['paint_scheme_id'] = paint_scheme.id
        serializer = RailroadCompanyPaintSchemeInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, company_id=None, paint_scheme_id=None, pk=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(RailroadCompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        queryset = RailroadCompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyPaintSchemeInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, company_id=None, paint_scheme_id=None, pk=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(RailroadCompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        queryset = RailroadCompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyPaintSchemeInformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, company_id=None, paint_scheme_id=None, pk=None):
        company = get_object_or_404(RailroadCompany.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(RailroadCompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        queryset = RailroadCompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)
        information = get_object_or_404(queryset, pk=pk)
        serializer = RailroadCompanyPaintSchemeInformationSerializer(information)
        return Response(serializer.data)
