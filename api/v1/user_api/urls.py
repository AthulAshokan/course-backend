from django.urls import path
from .views import RegisterUserView

app_name = 'user_api'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    
]


