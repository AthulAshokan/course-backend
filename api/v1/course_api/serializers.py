from rest_framework import serializers
from courses.models import MainCategory, SubCategory,Course,Curriculum

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'image', 'description']

class SubCategorySerializer(serializers.ModelSerializer):
    main_category = MainCategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'main_category', 'name', 'title', 'description', 'image']



class CourseSerializer(serializers.ModelSerializer):
    # Display full details in GET response
    main_category = MainCategorySerializer(read_only=True)
    sub_category = SubCategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = [  'id', 'price', 'skill_level', 'instructor','language', 'rating', 'certificate_image',
                   'is_active','main_category', 'sub_category']


class CurriculumSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
  
    class Meta:
        model = Curriculum
        fields = ['id', 'name', 'title', 'description', 'cover_image', 'what_will_you_learn', 'requirements', 'course']
  
      


