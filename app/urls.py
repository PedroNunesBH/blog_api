from django.contrib import admin
from django.urls import path
from users.views import ListBlogUsers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_users/', ListBlogUsers.as_view(), name="list_users")
]
