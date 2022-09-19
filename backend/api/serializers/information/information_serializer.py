from typing import List

from django.db.models import Sum
from django.utils import timezone
from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_effect_serializer import InformationEffectSerializer
from api.serializers.user.user_basic_info_serializer import UserBasicInfoSerializer
from core.models import InformationEffect, User
from core.models.information.information_model import Information
from core.models.information.information_vote_model import InformationVote


class InformationSerializer(GenericAuditedModelSerializer):
    author = UserBasicInfoSerializer()
    effects = InformationEffectSerializer(many=True)
    votes_up = serializers.SerializerMethodField('get_votes_up')
    votes_down = serializers.SerializerMethodField('get_votes_down')
    votes_sum = serializers.SerializerMethodField('get_votes_sum')

    @staticmethod
    def get_votes_up(obj):
        return len(InformationVote.objects.filter(information=obj, value__gt=0))

    @staticmethod
    def get_votes_down(obj):
        return len(InformationVote.objects.filter(information=obj, value__lt=0))

    @staticmethod
    def get_votes_sum(obj):
        return InformationVote.objects.filter(information=obj).aggregate(Sum('value'))['value__sum']

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

        self._create_effects_from_data(
            effects_data=effects_data,
            information=information,
            created_by=validated_data['created_by'].id
        )

        return information

    def update(self, instance: Information, validated_data):
        existing_effects = InformationEffect.objects.filter(information=instance)
        for existing_effect in existing_effects:
            existing_effect.delete()

        effects_data = validated_data.pop('effects')
        self._create_effects_from_data(
            effects_data=effects_data,
            information=instance,
            created_by=validated_data['updated_by'].id
        )

        return super(InformationSerializer, self).update(instance=instance, validated_data=validated_data)

    def _create_effects_from_data(self, effects_data: List, information: Information, created_by: str):
        for effect_data in effects_data:
            effect_data['information_id'] = str(information.id)
            effect_data['created_at'] = timezone.now()
            effect_data['created_by'] = created_by

            effect_serializer = InformationEffectSerializer(data=effect_data)
            effect_serializer.is_valid(raise_exception=True)
            effect_serializer.save()

    # Called on create/update operations
    def to_internal_value(self, data):
         self.fields['author'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

         return super(InformationSerializer, self).to_internal_value(data)

    # Called when reading
    def to_representation(self, obj):
        self.fields['author'] = UserBasicInfoSerializer()

        return super(InformationSerializer, self).to_representation(obj)
