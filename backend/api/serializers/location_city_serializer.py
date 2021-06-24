from api.models import LocationCity
from .generic_model_serializer import GenericModelSerializer
from .location_state_serializer import LocationStateSerializer


class LocationCitySerializer(GenericModelSerializer):
    state = LocationStateSerializer(write_only=True)

    class Meta:
        model = LocationCity
        fields = '__all__'
