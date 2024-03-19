from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post


class ListPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer


class DetailUpdateAndDeletePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
