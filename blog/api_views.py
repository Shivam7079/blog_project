from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, Comment, Profile

from .serializers import (
    PostSerializer,
    CommentSerializer,
    ProfileSerializer
)


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('-id')

    serializer_class = PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-id')

    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all().order_by('-id')

    serializer_class = ProfileSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]