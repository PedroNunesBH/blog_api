from django.urls import path
from .views import ListComments, CreateComments, DetailUpdateAndDeleteComments

urlpatterns = [
    path('list_comments/', ListComments.as_view(), name="list_comments"),
    path('create_comments/', CreateComments.as_view(), name="create_comments"),
    path('comment/<int:pk>/', DetailUpdateAndDeleteComments.as_view(), name="detail_update_delete_comment")
]
