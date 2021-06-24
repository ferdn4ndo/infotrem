from api.models import BilletGateway
from api.serializers import BilletGatewaySerializer
from api.services import policy
from .generic_model_view import ReadModelViewSet


class BilletGatewayViewSet(ReadModelViewSet):
    queryset = BilletGateway.objects.all()
    serializer_class = BilletGatewaySerializer
    permission_classes = [policy.IsLoggedIn, policy.IsAdminOrDeny]
