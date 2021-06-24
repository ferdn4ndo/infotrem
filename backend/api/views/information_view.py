from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from infotrem.models.information_model import Information, InformationEffect, InformationVote
from infotrem.serializers.information_serializer import InformationSerializer, InformationEffectSerializer, \
    InformationVoteSerializer
from infotrem.services.policy import IsLoggedIn, IsCreatorOrModeratorOrReadOnly, IsCreatorOrReadOnly


class InformationViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsCreatorOrModeratorOrReadOnly]

    def list(self, request):
        queryset = Information.objects.all()
        serializer = InformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = Information.objects.all()
        information = get_object_or_404(queryset, pk=pk)
        serializer = InformationSerializer(information)
        info_dict = serializer.data
        info_dict['vote'] = InformationVoteSerializer.get_value_for_user(information=information, user=request.user)
        return info_dict

    def partial_update(self, request, pk=None):
        queryset = Information.objects.all()
        information = get_object_or_404(queryset, pk=pk)
        serializer = InformationSerializer(information, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # ToDo: update vote for user
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Information.objects.all()
        information = get_object_or_404(queryset, pk=pk)
        serializer = InformationSerializer(information)
        return Response(serializer.data)


class InformationEffectViewSet(viewsets.ViewSet):
    permission_classes = [IsLoggedIn, IsCreatorOrModeratorOrReadOnly]

    def list(self, request, information_id=None):
        information = get_object_or_404(Information.objects.all(), pk=information_id)
        queryset = InformationEffect.objects.filter(information=information)
        serializer = InformationEffectSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, information_id=None):
        data = request.data
        data['information_id'] = information_id
        serializer = InformationEffectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, information_id=None, pk=None):
        information = get_object_or_404(Information.objects.all(), pk=information_id)
        queryset = InformationEffect.objects.filter(information=information)
        information_effect = get_object_or_404(queryset, pk=pk)
        serializer = InformationEffectSerializer(information_effect)
        return Response(serializer.data)

    def partial_update(self, request, information_id=None, pk=None):
        information = get_object_or_404(Information.objects.all(), pk=information_id)
        queryset = InformationEffect.objects.filter(information=information)
        information_effect = get_object_or_404(queryset, pk=pk)
        serializer = InformationEffectSerializer(information_effect)
        return Response(serializer.data)

    def destroy(self, request, information_id=None, pk=None):
        information = get_object_or_404(Information.objects.all(), pk=information_id)
        queryset = InformationEffect.objects.filter(information=information)
        information_effect = get_object_or_404(queryset, pk=pk)
        serializer = InformationEffectSerializer(information_effect)
        return Response(serializer.data)
