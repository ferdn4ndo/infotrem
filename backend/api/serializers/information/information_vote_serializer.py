from rest_framework import serializers

from api.serializers.generic_audited_model_serializer import GenericAuditedModelSerializer
from core.models.information.information_vote_model import InformationVote


class InformationVoteSerializer(GenericAuditedModelSerializer):
    information_id = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = InformationVote
        fields = [
            'id',
            'information_id',
            'value',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        ]

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
