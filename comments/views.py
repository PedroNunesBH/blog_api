from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import CommentSerializer
from .models import Comment


class ListComments(generics.ListAPIView):
    queryset = Comment.objects.all().filter(status="Aprovado")  # Apenas lista os comentarios aprovados
    serializer_class = CommentSerializer


class CreateComments(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )


class DetailUpdateAndDeleteComments(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly)
