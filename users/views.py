from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogUserSerializer
from .models import BlogUser


class ListBlogUsers(generics.ListAPIView):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer
