from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=64)
    password = serializers.CharField(required=True, max_length=64)
