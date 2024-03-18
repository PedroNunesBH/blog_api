from django.contrib import admin
from django.urls import path
from users.views import ListBlogUsers, CreateBlogUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_users/', ListBlogUsers.as_view(), name="list_users"),
    path('create_users/', CreateBlogUser.as_view(), name="create_users")
]
