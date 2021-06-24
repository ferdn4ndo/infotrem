from api.models import LocationState
from .generic_model_serializer import GenericModelSerializer


class LocationStateSerializer(GenericModelSerializer):
    class Meta:
        model = LocationState
        fields = '__all__'
