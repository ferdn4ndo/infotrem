from rest_framework import serializers

from core.models.user.user_model import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'email_validated',
            'email_validation_sent',
            'email_validation_hash',
            'name',
            'cpf',
            'birth_date',
            'address',
            'number',
            'complement',
            'city',
            'state',
            'zipcode',
            'phone',
            'is_admin',
            'is_staff',
            'is_active',
            'registered_at',
            'last_activity_at',
            'updated_at',
        ]
