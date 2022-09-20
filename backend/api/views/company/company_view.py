from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers.company.company_serializer import CompanySerializer
from api.policies.is_staff_or_read_only_policy import IsStaffOrReadOnlyPolicy
from core.models import Company


class CompanyViewSet(viewsets.ViewSet):
    permission_classes = [IsStaffOrReadOnlyPolicy]

    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company)
        return serializer.data

    def partial_update(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
