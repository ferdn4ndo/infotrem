from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers

from api.models.information_model import Information
from api.models.information_effect_model import InformationEffect
from api.models.information_vote_model import InformationVote
from api.serializers.user_serializer import UserSerializer


class InformationEffectSerializer(serializers.ModelSerializer):
    information_id = serializers.CharField(required=True, write_only=True)
    old_value = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = InformationEffect
        fields = ['information_id', 'field_name', 'old_value', 'new_value']


class InformationSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    created_by = UserSerializer()
    updated_by = UserSerializer()
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
        for effect_data in effects_data:
            InformationEffect.objects.create(information=information, **effect_data)
        return information


class InformationVoteSerializer(serializers.ModelSerializer):
    information = InformationSerializer(write_only=True)

    class Meta:
        model = InformationVote
        fields = ['information', 'value']

    @staticmethod
    def get_value_for_user(information: Information, user: User):
        try:
            vote = InformationVote.objects.get(information=information, voter=user)
            return vote.value
        except InformationVote.DoesNotExist:
            return 0

    @staticmethod
    def check_vote_value(vote_value):
        max_value, min_value = InformationVote.POSITIVE_VOTE_VALUE, InformationVote.NEGATIVE_VOTE_VALUE
        if vote_value > max_value or vote_value < min_value:
            raise serializers.ValidationError(
                'Vote value may not be greater than {} and lower than {}'.format(max_value, min_value)
            )

    def create(self, validated_data):
        self.check_vote_value(validated_data['value'])
        return InformationVote.objects.create(**validated_data)

    def update(self, instance, validated_data):
        self.check_vote_value(validated_data['value'])
        instance.value = validated_data['value']
        instance.save()
        return instance
