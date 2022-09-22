from rest_framework.request import Request
from rest_framework.response import Response

from api.errors.conflict_exception import ConflictException
from api.models import get_object_or_404
from api.serializers.information.information_vote_serializer import InformationVoteSerializer
from api.policies.is_logged_in_policy import IsLoggedInPolicy
from api.pagination.large_results_set_pagination import LargeResultsSetPagination
from api.views.generic_model_view import FullCRUDListModelViewSet
from core.models import ensure_object_owner_or_deny
from core.models.information.information_model import Information
from core.models.information.information_vote_model import InformationVote
from core.services.information.information_vote_service import InformationVoteService
from core.services.user.user_permissions_service import UserPermissionsService


class InformationVoteViewSet(FullCRUDListModelViewSet):
    permission_classes = [IsLoggedInPolicy]
    serializer_class = InformationVoteSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        information = get_object_or_404(Information.objects.all(), id=self.kwargs['information_id'])

        service = UserPermissionsService(user=self.request.user)
        if service.is_admin_or_staff():
            return InformationVote.objects.filter(information=information)

        return InformationVote.objects.filter(information=information, created_by=self.request.user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        information = get_object_or_404(Information.objects.all(), id=self.kwargs['information_id'])
        service = InformationVoteService(information=information)
        if service.has_user_voted(user=request.user):
            raise ConflictException("You have already voted on this information.")

        request.data['information_id'] = self.kwargs['information_id']

        return super(InformationVoteViewSet, self).create(request=request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        ensure_object_owner_or_deny(user=request.user, model_type=InformationVote, pk=kwargs['pk'])

        request.data['information_id'] = self.kwargs['information_id']

        return super(InformationVoteViewSet, self).update(request=request, *args, **kwargs)
