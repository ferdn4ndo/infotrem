from rest_framework import serializers

from infotrem.models.information import Information, InformationEffect, InformationVote
from infotrem.serializers.user import UserSerializer


class InformationEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationEffect
        fields = ['field_name', 'old_value', 'new_value']


class InformationSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    created_by = UserSerializer()
    updated_by = UserSerializer()
    effects = InformationEffectSerializer(many=True)

    class Meta:
        model = Information
        fields = [
            'id',
            'author',
            'content',
            'effects',
            'status',
            'references',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
            'votes_up',
            'votes_down',
            'votes_sum',
        ]

    def create(self, validated_data):
        effects_data = validated_data.pop('effects')
        information = Information.objects.create(**validated_data)
        for effect_data in effects_data:
            InformationEffect.objects.create(information=information, **effect_data)
        return information


class InformationVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationVote
        fields = '__all__'
