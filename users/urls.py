from django.urls import path
from .views import ListBlogUsers, CreateBlogUser, DetailUpdateAndDeleteBlogUser


urlpatterns = [
    path('list_users/', ListBlogUsers.as_view(), name="list_users"),
    path('create_users/', CreateBlogUser.as_view(), name="create_users"),
    path('user/<int:pk>/', DetailUpdateAndDeleteBlogUser.as_view(), name="detail_update_delete_user"),
]
