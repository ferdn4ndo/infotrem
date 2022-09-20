from django.db.models import Sum
from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from api.serializers.information.information_effect_serializer import InformationEffectSerializer
from api.serializers.user.user_basic_info_serializer import UserBasicInfoSerializer
from core.services.information.information_service import InformationService
from core.models import User
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
        return InformationService.create_information_from_data(
            information_data=validated_data,
            created_by=validated_data['created_by']
        )

    def update(self, instance: Information, validated_data):
        return InformationService.update_information_from_data(
            information_data=validated_data,
            information=instance,
            updated_by=validated_data['updated_by']
        )

    # Called on create/update operations
    def to_internal_value(self, data):
         self.fields['author'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

         return super(InformationSerializer, self).to_internal_value(data)

    # Called when reading
    def to_representation(self, obj):
        self.fields['author'] = UserBasicInfoSerializer()

        return super(InformationSerializer, self).to_representation(obj)
