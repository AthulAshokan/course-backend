from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MainCategoryViewSet, SubCategoryViewSet, CourseViewSet

# Router for ViewSets
router = DefaultRouter()
router.register(r'main-categories', MainCategoryViewSet)
router.register(r'sub-categories', SubCategoryViewSet)
router.register(r'courses', CourseViewSet)

app_name = 'course_api'

urlpatterns = [
    path('', include(router.urls)),
]