from rest_framework import serializers

from infotrem.models.storage import StorageFile
from infotrem.services.amazon import get_expirable_download_url


class StorageFileSerializer(serializers.ModelSerializer):
    mime_type = serializers.CharField(max_length=255)
    storage_file_path = serializers.CharField(max_length=1024, required=False)

    class Meta:
        model = StorageFile
        fields = '__all__'

    def to_representation(self, instance):
        instance_dict = super(StorageFileSerializer, self).to_representation(instance)
        instance_dict['url'] = get_expirable_download_url(instance)
        return instance_dict
