from rest_framework import serializers
from courses.models import MainCategory, SubCategory,Course

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'image', 'description']

class SubCategorySerializer(serializers.ModelSerializer):
    maincategory = MainCategorySerializer(read_only=True)
    maincategory_id = serializers.PrimaryKeyRelatedField(
        queryset=MainCategory.objects.all(),
        source='maincategory'
    )

    class Meta:
        model = SubCategory
        fields = ['id', 'maincategory', 'maincategory_id', 'name', 'title', 'description', 'image']



class CourseSerializer(serializers.ModelSerializer):
    # Display full details in GET response
    main_category = MainCategorySerializer(read_only=True)
    sub_category = SubCategorySerializer(read_only=True)

    # Accept only category IDs when creating/updating
    main_category_id = serializers.PrimaryKeyRelatedField(
        queryset=MainCategory.objects.all(), 
        source='main_category', 
        write_only=True
    )
    sub_category_id = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all(), 
        source='sub_category', 
        write_only=True
    )

    class Meta:
        model = Course
        fields = [
    'id', 'price', 'skill_level', 'main_category', 'sub_category',
    'main_category_id', 'sub_category_id', 'instructor',
    'language', 'rating', 'certificate_image', 'is_active'
]

