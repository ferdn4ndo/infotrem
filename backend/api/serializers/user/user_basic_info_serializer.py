from rest_framework import serializers

from core.models.user.user_model import User


class UserBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'is_active',
            'registered_at',
            'last_activity_at',
            'updated_at',
        ]
