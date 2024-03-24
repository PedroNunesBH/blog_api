from django.urls import path
from .views import (ListPosts, CreatePost, DetailUpdateAndDeletePost, PostLikeView,
                    PostDislikeView, ListPostByCategorieView, PostStatsView)


urlpatterns = [
    path('list_posts/', ListPosts.as_view(), name="list_posts"),
    path('create_posts/', CreatePost.as_view(), name="create_posts"),
    path('post/<int:pk>/', DetailUpdateAndDeletePost.as_view(), name="detail_update_delete_post"),
    path('post/like/<int:pk>/', PostLikeView.as_view(), name="post_like"),
    path('post/dislike/<int:pk>/', PostDislikeView.as_view(), name="post_dislike"),
    path('posts/<str:category>/', ListPostByCategorieView.as_view(), name="post_by_category"),
    path('posts/stats', PostStatsView.as_view(), name="post_stats")
]
