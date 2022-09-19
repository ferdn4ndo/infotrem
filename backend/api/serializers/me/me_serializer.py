from rest_framework import serializers

from api.models import get_object_or_404
from core.models.location.location_city_model import LocationCity
from core.models.location.location_state_model import LocationState
from core.models.user.user_model import User


class MeSerializer(serializers.ModelSerializer):
    is_admin = serializers.ReadOnlyField()
    is_staff = serializers.ReadOnlyField()
    is_active = serializers.ReadOnlyField()
    registered_at = serializers.ReadOnlyField()
    last_activity_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    state_id = serializers.UUIDField(required=False, write_only=True)
    city_id = serializers.UUIDField(required=False, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'cpf',
            'birth_date',
            'address',
            'number',
            'complement',
            'city',
            'city_id',
            'state',
            'state_id',
            'zipcode',
            'phone',
            'is_admin',
            'is_staff',
            'is_active',
            'registered_at',
            'last_activity_at',
            'updated_at',
        ]

    def update(self, instance, validated_data):
        if 'state_id' in validated_data:
            state_id = validated_data.pop('state_id')
            validated_data['state'] = get_object_or_404(LocationState.objects.all(), id=state_id)

        if 'city_id' in validated_data:
            city_id = validated_data.pop('city_id')
            validated_data['city'] = get_object_or_404(LocationCity.objects.all(), id=city_id)

        return super(MeSerializer, self).update(instance, validated_data)
