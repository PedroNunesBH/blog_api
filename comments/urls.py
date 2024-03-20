from django.urls import path
from .views import ListComments

urlpatterns = [
    path('list_comments/', ListComments.as_view(), name="list_comments"),
]
