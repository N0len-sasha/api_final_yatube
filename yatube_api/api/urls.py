from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = SimpleRouter()
router.register(
    r'posts',
    PostViewSet
)
router.register(
    r'groups',
    GroupViewSet
)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register(
    r'^posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)$',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/follow/', FollowViewSet.as_view()),
    path('v1/', include('djoser.urls.jwt')),
]
