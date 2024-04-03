from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import DefaultUserSerializer
from django.contrib.auth.models import User
from .permissions import IsAdminOrCreateOnly


class ListAndCreateBlogUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = DefaultUserSerializer
    permission_classes = (IsAdminOrCreateOnly, )  # Apenas users administradores podem GET e POST qualquer user


class DetailUpdateAndDeleteBlogUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DefaultUserSerializer
    permission_classes = (IsAdminUser, )
