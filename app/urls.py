from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('comments.urls')),
    path('api/v1', include('authentication.urls'))
]
