from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import DefaultUserSerializer
from django.contrib.auth.models import User


class ListBlogUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = DefaultUserSerializer
    permission_classes = (IsAdminUser, )  # Apenas usuarios administradores


class CreateBlogUser(generics.CreateAPIView):
    serializer_class = DefaultUserSerializer


class DetailUpdateAndDeleteBlogUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DefaultUserSerializer
    permission_classes = (IsAdminUser, )
