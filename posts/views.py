from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post


class ListPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )


class DetailUpdateAndDeletePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )  # Usuarios não autenticados podem apenas visualizar
