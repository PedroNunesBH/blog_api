from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('users.urls')),
    path('', include('comments.urls')),
    path('', include('authentication.urls'))
]
