from rest_framework import serializers
from courses.models import MainCategory, SubCategory,Course,Curriculum,Module

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
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Curriculum
        fields = "__all__"

class Moduleserializer(serializers.ModelSerializer):
    Curriculum = CurriculumSerializer(read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'module_name', 'title', 'description', 'video_url', 'video_title', 'video_description', 'notes', 'notes_title', 'image', 'is_free', 'Curriculum']
  
      


