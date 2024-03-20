from django.urls import path
from .views import ListComments, CreateComments

urlpatterns = [
    path('list_comments/', ListComments.as_view(), name="list_comments"),
    path('create_comments/', CreateComments.as_view(), name="create_comments"),
]
