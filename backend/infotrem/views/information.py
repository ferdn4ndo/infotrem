from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from infotrem.models.information import Information, InformationEffect, InformationVote
from infotrem.serializers.information import InformationSerializer, InformationEffectSerializer, \
    InformationVoteSerializer
from infotrem.services.policy import IsLoggedIn, IsCreatorOrModeratorOrReadOnly


class InformationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsCreatorOrModeratorOrReadOnly]

    def list(self, request):
        queryset = Information.objects.all()
        serializer = InformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, information_id=None):
        queryset = Information.objects.all()
        information = get_object_or_404(queryset, pk=information_id)
        serializer = InformationSerializer(information)
        return Response(serializer.data)

    def partial_update(self, request, information_id=None):
        queryset = Information.objects.all()
        information = get_object_or_404(queryset, pk=information_id)
        serializer = InformationSerializer(information)
        return Response(serializer.data)

    def destroy(self, request, information_id=None):
        queryset = Information.objects.all()
        information = get_object_or_404(queryset, pk=information_id)
        serializer = InformationSerializer(information)
        return Response(serializer.data)


class InformationEffectList(generics.ListCreateAPIView):
    queryset = InformationEffect.objects.all()
    serializer_class = InformationEffectSerializer
    permission_classes = [IsAuthenticated]


class InformationEffectRetrieve(generics.RetrieveAPIView):
    queryset = InformationEffect.objects.all()
    serializer_class = InformationEffectSerializer
    permission_classes = [IsAuthenticated]


class InformationVoteList(generics.ListCreateAPIView):
    queryset = InformationVote.objects.all()
    serializer_class = InformationVoteSerializer
    permission_classes = [IsAuthenticated]


class InformationVoteRetrieve(generics.RetrieveAPIView):
    queryset = InformationVote.objects.all()
    serializer_class = InformationVoteSerializer
    permission_classes = [IsAuthenticated]


class InformationVoteUpdateDestroy(generics.RetrieveAPIView):
    serializer_class = InformationVoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InformationVote.objects.filter(created_by=self.request.user)
