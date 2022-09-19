from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views.album.album_comment_view import AlbumCommentViewSet
from api.views.album.album_view import AlbumViewSet


router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=AlbumViewSet,
    basename=RouteNames.ROUTE_ALBUM
)

router.register(
    prefix=r'(?P<album_id>[^/.]+)/comments',
    viewset=AlbumCommentViewSet,
    basename=RouteNames.ROUTE_ALBUM_COMMENT
)

urlpatterns = router.urls
