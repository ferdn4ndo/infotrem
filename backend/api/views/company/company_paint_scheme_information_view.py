from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers.company.company_paint_scheme_information_serializer import CompanyPaintSchemeInformationSerializer
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from core.models import Company, CompanyPaintScheme, CompanyPaintSchemeInformation


class CompanyPaintSchemeInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]

    def list(self, request, company_id=None, paint_scheme_id=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(CompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        paint_scheme_queryset = CompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)
        serializer = CompanyPaintSchemeInformationSerializer(paint_scheme_queryset, many=True)
        return Response(serializer.data)

    def create(self, request, company_id=None, paint_scheme_id=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(CompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        data = request.data
        data['paint_scheme_id'] = paint_scheme.id
        serializer = CompanyPaintSchemeInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, company_id=None, paint_scheme_id=None, pk=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(CompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        queryset = CompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)
        information = get_object_or_404(queryset, pk=pk)
        serializer = CompanyPaintSchemeInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, company_id=None, paint_scheme_id=None, pk=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(CompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        queryset = CompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)
        information = get_object_or_404(queryset, pk=pk)
        serializer = CompanyPaintSchemeInformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, company_id=None, paint_scheme_id=None, pk=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        paint_scheme = get_object_or_404(CompanyPaintScheme.objects.all(), pk=paint_scheme_id)
        queryset = CompanyPaintSchemeInformation.objects.filter(paint_scheme=paint_scheme)
        information = get_object_or_404(queryset, pk=pk)
        serializer = CompanyPaintSchemeInformationSerializer(information)
        return Response(serializer.data)
