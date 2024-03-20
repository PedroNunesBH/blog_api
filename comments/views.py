from django.shortcuts import render
from rest_framework import generics
from .serializers import CommentSerializer
from .models import Comment


class ListComments(generics.ListAPIView):
    queryset = Comment.objects.all().filter(status="Aprovado")  # Apenas lista os comentarios aprovados
    serializer_class = CommentSerializer


class CreateComments(generics.CreateAPIView):
    serializer_class = CommentSerializer
