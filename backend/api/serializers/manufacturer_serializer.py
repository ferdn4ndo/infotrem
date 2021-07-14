from rest_framework import serializers

from api.models import ManufacturerInformation
from api.models.information_model import Information
from api.models.manufacturer_model import Manufacturer
from api.serializers.information_serializer import InformationSerializer


class ManufacturerInformationSerializer(serializers.ModelSerializer):
    manufacturer_id = serializers.CharField(required=True, write_only=True)
    information = InformationSerializer()

    class Meta:
        model = ManufacturerInformation
        fields = ['id', 'manufacturer_id', 'information']

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.create(**information_data)
        manufacturer = Manufacturer.objects.get(id=validated_data['manufacturer_id'])
        return ManufacturerInformation.objects.create(manufacturer=manufacturer, information=information)

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information')
        information = Information.objects.get(id=information_data['id'])
        serializer = InformationSerializer(information, data=information_data)
        serializer.save()
        instance.information = information
        instance.save()
        return instance


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'
