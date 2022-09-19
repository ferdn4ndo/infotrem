from api.serializers.generic_model_serializer import GenericModelSerializer
from api.serializers.location_state_serializer import LocationStateSerializer
from core.models.location.location_city_model import LocationCity


class LocationCitySerializer(GenericModelSerializer):
    state = LocationStateSerializer(write_only=True)

    class Meta:
        model = LocationCity
        fields = '__all__'
