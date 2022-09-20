from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers.company.company_paint_scheme_serializer import CompanyPaintSchemeSerializer
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from core.models import Company, CompanyPaintScheme


class CompanyPaintSchemeViewSet(viewsets.ViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]

    def list(self, request, company_id=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        queryset = CompanyPaintScheme.objects.filter(railroad=company)
        serializer = CompanyPaintSchemeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, company_id=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        queryset = CompanyPaintScheme.objects.filter(railroad=company)
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanyPaintSchemeSerializer(company)
        return serializer.data

    def partial_update(self, request, pk=None, company_id=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        queryset = CompanyPaintScheme.objects.filter(railroad=company)
        paint_scheme = get_object_or_404(queryset, pk=pk)
        serializer = CompanyPaintSchemeSerializer(paint_scheme, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None, company_id=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        queryset = CompanyPaintScheme.objects.filter(railroad=company)
        paint_scheme = get_object_or_404(queryset, pk=pk)
        serializer = CompanyPaintSchemeSerializer(paint_scheme)
        return Response(serializer.data)
