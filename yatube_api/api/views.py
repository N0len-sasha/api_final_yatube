from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters, status, viewsets, permissions
from rest_framework.response import Response


from .permissions import IsAuthorOrReadOnly
from .serializers import (PostSerializer,
                          GroupSerializer,
                          CommentSerializer,
                          FollowSerializer)
from posts.models import Post, Group


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), author=self.request.user)


class FollowViewSet(viewsets.ViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ('following__username',)

    def list(self, request):
        search_param = self.request.query_params.get('search')
        queryset = request.user.follower.all()

        if search_param:
            queryset = queryset.filter(
                following__username__icontains=search_param)

        serializer = FollowSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        following_username = request.data.get('following')

        if request.user.follower.filter(
                following__username=following_username).exists():
            return Response({'detail': 'Вы уже подписаны на этого автора.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if following_username == request.user.username:
            return Response({'detail': 'Нельзя подписаться на самого себя.'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
