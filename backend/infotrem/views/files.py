from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import authentication, permissions
from rest_framework import generics

from infotrem.models.storage import StorageFile
from infotrem.serializers.storage import StorageFileSerializer


class ListUploadedFiles(generics.ListAPIView):
    """
    View to list all files in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    queryset = StorageFile.objects.all()
    serializer_class = StorageFileSerializer
