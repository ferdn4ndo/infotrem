from rest_framework import serializers

from core.models import LocomotiveDesign


class RollingStockLocomotiveModelSerializer(serializers.ModelSerializer):
    """Serializer for the LocomotiveDesign model"""

    class Meta:
        model = LocomotiveDesign
        excludes = ['rolling_stock']
