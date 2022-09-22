from rest_framework.request import Request
from rest_framework.response import Response

from api.models import get_object_or_404
from api.policies.is_logged_in_or_read_only_policy import IsLoggedInOrReadOnlyPolicy
from api.serializers.information.information_effect_serializer import InformationEffectSerializer
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import ensure_object_owner_or_deny
from core.models.information.information_effect_model import InformationEffect
from core.models.information.information_model import Information


class InformationEffectViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInOrReadOnlyPolicy]
    serializer_class = InformationEffectSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        information = get_object_or_404(Information.objects.all(), id=self.kwargs['information_id'])

        return InformationEffect.objects.filter(information=information)

    def create(self, request: Request, *args, **kwargs) -> Response:
        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = Information.InformationStatus.DISCUSSION

        request.data['information_id'] = self.kwargs['information_id']

        return super(InformationEffectViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(user=request.user, model_type=InformationEffect, pk=kwargs['pk'])

        instance = get_object_or_404(InformationEffect.objects.all(), pk=kwargs['pk'])
        if not request.user.is_staff and not request.user.is_admin:
            request.data['status'] = instance.status

        request.data['information_id'] = self.kwargs['information_id']

        return super(InformationEffectViewSet, self).update(request=request, *args, **kwargs)
