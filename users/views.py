from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import BlogUserSerializer
from .models import BlogUser


class ListBlogUsers(generics.ListAPIView):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer
    permission_classes = (IsAdminUser, )  # Apenas usuarios administradores


class CreateBlogUser(generics.CreateAPIView):
    serializer_class = BlogUserSerializer


class DetailUpdateAndDeleteBlogUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer
    permission_classes = (IsAdminUser, )
