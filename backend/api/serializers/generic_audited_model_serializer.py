from rest_framework import serializers

from api.models import User

from .generic_model_serializer import GenericModelSerializer


class GenericAuditedModelSerializer(GenericModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )
    created_at = serializers.DateTimeField()
    updated_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )
    updated_at = serializers.DateTimeField(
        required=False,
        allow_null=True,
    )
