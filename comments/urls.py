from django.urls import path
from .views import ListAndCreateComments, DetailUpdateAndDeleteComments

urlpatterns = [
    path('comments/', ListAndCreateComments.as_view(), name="list_and_create_comments"),
    path('comment/<int:pk>/', DetailUpdateAndDeleteComments.as_view(), name="detail_update_delete_comment")
]
