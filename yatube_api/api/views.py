from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings

from .permissions import IsAuthorOrReadOnlly
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentsSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [
        *api_settings.DEFAULT_PERMISSION_CLASSES,
        IsAuthorOrReadOnlly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, **kwargs):
        post = self.get_object()
        if request.method == 'POST':
            serializer = CommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user, post=post)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        comments = Comment.objects.filter(post=post)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [
        *api_settings.DEFAULT_PERMISSION_CLASSES,
        IsAuthorOrReadOnlly]


class GroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
