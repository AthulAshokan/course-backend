from rest_framework import viewsets
from courses.models import MainCategory, SubCategory, Course
from .serializers import MainCategorySerializer, SubCategorySerializer, CourseSerializer

# MainCategory ViewSet
class MainCategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer

# SubCategory ViewSet
class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

# Course ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

