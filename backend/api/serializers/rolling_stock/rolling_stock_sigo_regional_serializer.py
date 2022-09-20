from rest_framework import serializers

from api.serializers.company.company_serializer import CompanySerializer
from core.models import SigoRegional


class RollingStockSigoRegionalSerializer(serializers.ModelSerializer):
    """Serializer for the SigoRegional model"""
    original_company = CompanySerializer(required=False)

    class Meta:
        model = SigoRegional
        fields = '__all__'
