from django.urls import path
from .views import RegisterUserView

from .views import LoginView, OTPVerificationView

app_name = 'user_api'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
]


