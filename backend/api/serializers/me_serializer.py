from rest_framework import serializers

from api.models import User, LocationState, get_object_or_404, LocationCity


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
            'rg',
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
            'relational_status',
            'education_level_self',
            'education_level_father',
            'education_level_mother',
            'has_children',
            'total_children',
            'youngest_child_birth_date',
            'skin_color_or_racial_group',
            'habitation_level',
            'family_income_level',
            'total_people_living_together',
            'financial_status',
            'job_status',
            'special_needs',
            'has_auditive_disability',
            'has_physical_disability',
            'has_mental_disability',
            'has_motor_disability',
            'has_visual_disability',
            'has_other_disability',
            'other_disability_detail',
            'disease_id',
            'doctor_name',
            'needs_accommodation',
            'needs_reader',
            'needs_enlarged_exam',
            'needs_typist',
            'needs_other',
            'other_needs_detail',
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
