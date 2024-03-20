from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('get_token/', TokenObtainPairView.as_view(), name="get_token"),
    path('verify_token/', TokenVerifyView.as_view(), name="verify_token"),
    path('refresh_token/', TokenRefreshView.as_view(), name="refresh_token")
]
