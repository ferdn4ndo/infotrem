from api.models import Billet
from api.serializers import BilletSerializer
from api.services import policy
from .generic_model_view import ReadModelViewSet


class BilletViewSet(ReadModelViewSet):
    queryset = Billet.objects.all()
    serializer_class = BilletSerializer
    permission_classes = [policy.IsLoggedIn, policy.IsAdminOrDeny]
