from django.contrib import admin
from django.urls import path
from users.views import ListBlogUsers, CreateBlogUser, DetailUpdateAndDeleteBlogUser
from posts.views import ListPosts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_users/', ListBlogUsers.as_view(), name="list_users"),
    path('create_users/', CreateBlogUser.as_view(), name="create_users"),
    path('user/<int:pk>/', DetailUpdateAndDeleteBlogUser.as_view(), name="detail_update_delete_user"),
    path('list_posts/', ListPosts.as_view(), name="list_posts")
]
