from rest_framework import viewsets, views, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from service.user_like import PostLikeManager
from social.models import Post
from social.permissions import IsPostOwner
from social.serializers.post import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsPostOwner])
    def update(self, request, pk=None):
        super(PostViewSet).update(self, request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAuthenticated, IsPostOwner])
    def destroy(self, request, pk=None):
        super(PostViewSet).destroy(self, request, pk)


class PostLikeViewSet(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        response = PostLikeManager(user=request.user).like_unlike(post)
        return Response(response, status=status.HTTP_200_OK)
