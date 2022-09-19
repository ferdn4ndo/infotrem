from rest_framework import routers

from api.routers.route_names import RouteNames
from api.views.comment.comment_view import CommentViewSet


router = routers.SimpleRouter()

router.register(
    prefix=r'',
    viewset=CommentViewSet,
    basename=RouteNames.ROUTE_COMMENT
)

urlpatterns = router.urls
