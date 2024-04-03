from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import CommentSerializer
from .models import Comment


class ListAndCreateComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all().filter(status="Aprovado")  # Apenas lista os comentarios aprovados
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class DetailUpdateAndDeleteComments(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
