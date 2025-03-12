from django.urls import path
from .views import RegisterUserView

from .views import LoginView, OTPVerificationView
from .views import UserProfileView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'user_api'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),

    path('login/', LoginView.as_view(), name='login'),

    path('verify-otp/', OTPVerificationView.as_view(), name='verify-otp'),

    path('profile/', UserProfileView.as_view(), name='profile'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]



