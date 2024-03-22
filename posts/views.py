from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db import models
from .serializers import PostSerializer
from .models import Post, PostLikeAndDislike


class ListPosts(generics.ListAPIView):
    queryset = Post.objects.filter(status="Aprovado")
    serializer_class = PostSerializer


class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )


class DetailUpdateAndDeletePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )  # Usuarios não autenticados podem apenas visualizar


class PostLikeView(generics.RetrieveAPIView):
    queryset = PostLikeAndDislike.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        user_pk = self.request.user.id  # Captura a primary key/ id do usuario
        post_pk = self.kwargs.get('pk')  # Captura a primary key/id do post
        like_exists = PostLikeAndDislike.objects.filter(user_id=user_pk, post_id=post_pk, like=True, dislike=False).exists()  # Procura por registro de um like do post pelo user
        print(like_exists)
        dislike_exists = PostLikeAndDislike.objects.filter(user_id=user_pk, post_id=post_pk, dislike=True)
        if like_exists:  # Verifica a existencia
            return None
        else:
            if dislike_exists:
                dislike_exists.update(dislike=False, like=True)
                Post.objects.filter(id=post_pk).update(dislikes=models.F('dislikes') - 1, likes=models.F('likes') + 1)
                return super().get_object()
            else:
                PostLikeAndDislike.objects.create(user_id=user_pk, post_id=post_pk, like=True)  # Cria o registro no BD
                Post.objects.filter(id=post_pk).update(likes=models.F('likes') + 1)
                return super().get_object()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is None:
            return JsonResponse({"Error": "O usuário já deu like nesse post"},
                                status=400)  # Retorna um erro se o usuário já deu like
        else:
            return JsonResponse({"Success": "Like efetuado com sucesso"})


class PostDislikeView(generics.RetrieveAPIView):
    queryset = PostLikeAndDislike.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        user_pk = self.request.user.id
        post_pk = self.kwargs.get('pk')
        dislike_exists = PostLikeAndDislike.objects.filter(user=user_pk, post=post_pk, dislike=True)
        like_exists = PostLikeAndDislike.objects.filter(user=user_pk, post=post_pk, like=True)
        if dislike_exists:
            return None
        else:
            if like_exists:
                like_exists.update(like=False, dislike=True)
                Post.objects.filter(id=post_pk).update(likes=models.F('likes') - 1, dislikes=models.F('dislikes') + 1)
                return super().get_object()
            else:
                PostLikeAndDislike.objects.create(user_id=user_pk, post_id=post_pk, dislike=True, like=False)
                Post.objects.filter(id=post_pk).update(dislikes=models.F('dislikes') + 1)
                return super().get_object()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is None:
            return JsonResponse({"Error": "O usuário já deu dislike nesse post"},
                                status=400)  # Retorna um erro se o usuário já deu like
        else:
            return JsonResponse({"Success": "Dislike efetuado com sucesso"})


class ListPostByCategorieView(generics.ListAPIView):  # Lista todos os posts da categoria especificada no endpoint
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        category = self.kwargs.get('category', None)  # Captura nos parametros do endpoint o valor de category passado
        print(self.kwargs)
        print(category)
        if category is not None:
            queryset = queryset.filter(category__icontains=category)  # Filtra pela categoria desejada
            return queryset
        return queryset
