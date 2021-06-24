from rest_framework import serializers


class SubscriptionEligibilitySerializer(serializers.Serializer):
    candidate = serializers.UUIDField(required=True)
    vacancy = serializers.UUIDField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
