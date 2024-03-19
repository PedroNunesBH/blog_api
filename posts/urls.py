from django.urls import path
from .views import ListPosts, CreatePost, DetailUpdateAndDeletePost


urlpatterns = [
    path('list_posts/', ListPosts.as_view(), name="list_posts"),
    path('create_posts/', CreatePost.as_view(), name="create_posts"),
    path('post/<int:pk>/', DetailUpdateAndDeletePost.as_view(), name="detail_update_delete_post")
]
