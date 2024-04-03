from django.urls import path
from .views import ListAndCreateBlogUsers, DetailUpdateAndDeleteBlogUser


urlpatterns = [
    path('users/', ListAndCreateBlogUsers.as_view(), name="list_and_create_users"),
    path('user/<int:pk>/', DetailUpdateAndDeleteBlogUser.as_view(), name="detail_update_delete_user"),
]
