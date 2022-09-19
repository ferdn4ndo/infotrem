from api.serializers.generic_model_serializer import GenericModelSerializer
from core.models.location.location_state_model import LocationState


class LocationStateSerializer(GenericModelSerializer):
    class Meta:
        model = LocationState
        fields = '__all__'
