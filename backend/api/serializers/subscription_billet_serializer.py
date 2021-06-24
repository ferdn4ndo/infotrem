from api.models import SubscriptionBillet
from .billet_serializer import BilletSerializer
from .generic_audited_model_serializer import GenericAuditedModelSerializer
from .subscription_serializer import SubscriptionSerializer


class SubscriptionBilletSerializer(GenericAuditedModelSerializer):
    subscription = SubscriptionSerializer(write_only=True)
    billet = BilletSerializer()

    class Meta:
        model = SubscriptionBillet
        fields = '__all__'
