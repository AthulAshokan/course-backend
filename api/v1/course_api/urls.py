from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router = DefaultRouter()
router.register(r'', CourseViewSet)

app_name = 'course_api'

urlpatterns = [
    path('', include(router.urls)),
]