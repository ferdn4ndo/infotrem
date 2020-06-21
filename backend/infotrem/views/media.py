import os
import pathlib

from django.contrib.auth.models import User
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from infotrem.errors import InvalidFileMimeType
from infotrem.models.media import MediaItemRollingStock, MediaItem
from infotrem.models.storage import StorageFile
from infotrem.serializers.media import MediaItemRollingStockSerializer, MediaItemSerializer, \
    MediaItemRollingStockFromNameSerializer
from infotrem.services.file import get_random_file_temp_path, save_from_memory


def index(request):
    return HttpResponse("Hello, world. You're at the views index.")




# @api_view(["POST"])
# def create_from_url(request):
#     if 'url' not in request.body:
#         return JsonResponse({'message': "Missing the 'url' key in body"}, status=400)
#
#     url = request.body['url']
#     if not check_if_url_is_downloadable(url):
#         return JsonResponse({'message': "The given URL "}, status=400)
#
#     file_uuid = get_new_unique_file_identifier('media')
#     uploaded_url = upload_from_url(url, file_uuid, 'media')
#
#     return JsonResponse({
#         'message': 'OK',
#         'fileUrl': uploaded_url,
#     })


@method_decorator(csrf_exempt, name='dispatch')
class UploadMedia(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    # throttle_classes = [UserRateThrottle]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        if 'file' not in request.FILES:
            return JsonResponse({'message': 'Missing file field in form data'}, status=400)

        print(request.POST)
        return JsonResponse([])

        temp_file = request.FILES['file']
        try:
            media_item = MediaItem.create_from_request_file(temp_file, request.user)
        except InvalidFileMimeType:
            return JsonResponse({'message': 'Only image and video files are allowed'}, status=400)

        return JsonResponse(MediaItemSerializer(media_item).data)


class MediaItemListView(generics.ListAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
    authentication_classes = [authentication.TokenAuthentication]


class MediaItemRollingStockView(generics.ListCreateAPIView):
    queryset = MediaItemRollingStock.objects.all()
    serializer_class = MediaItemRollingStockFromNameSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_media_item(self, media_uuid):
        try:
            media_item = MediaItem.objects.get(media_uuid=media_uuid)
        except MediaItem.DoesNotExist:
            raise Http404

        return media_item

    def perform_create(self, serializer: MediaItemRollingStockSerializer):
        serializer.save(created_by=self.request.user)

    def list(self, request, *args, **kwargs):
        media_item = self.get_media_item(media_uuid=kwargs['media_uuid'])
        queryset = MediaItemRollingStock.objects.filter(media_item=media_item)
        serializer = MediaItemRollingStockSerializer(queryset, many=True)
        return Response(serializer.data)
