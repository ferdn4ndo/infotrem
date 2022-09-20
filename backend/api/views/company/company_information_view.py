from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers.company.company_information_serializer import CompanyInformationSerializer
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from core.models import Company, CompanyInformation


class CompanyInformationViewSet(viewsets.ViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]

    def list(self, request, company_id=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        queryset = CompanyInformation.objects.filter(company=company)
        serializer = CompanyInformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, company_id=None):
        data = request.data
        data['company_id'] = company_id
        serializer = CompanyInformationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, company_id=None, pk=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        queryset = CompanyInformation.objects.filter(company=company)
        information = get_object_or_404(queryset, pk=pk)
        serializer = CompanyInformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, company_id=None, pk=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        queryset = CompanyInformation.objects.filter(company=company)
        information = get_object_or_404(queryset, pk=pk)
        serializer = CompanyInformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, company_id=None, pk=None):
        company = get_object_or_404(Company.objects.all(), pk=company_id)
        queryset = CompanyInformation.objects.filter(company=company)
        information = get_object_or_404(queryset, pk=pk)
        serializer = CompanyInformationSerializer(information)
        return Response(serializer.data)
