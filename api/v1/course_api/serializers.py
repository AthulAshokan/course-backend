from rest_framework import serializers
from courses.models import MainCategory, SubCategory, Course

# MainCategory Serializer
class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'image']

# SubCategory Serializer
class SubCategorySerializer(serializers.ModelSerializer):
    main_category = MainCategorySerializer(read_only=True)
    main_category_id = serializers.PrimaryKeyRelatedField(
        queryset=MainCategory.objects.all(), write_only=True
    )

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'title', 'description', 'image', 'main_category', 'main_category_id']

    def create(self, validated_data):
        main_category = validated_data.pop('main_category_id')
        sub_category = SubCategory.objects.create(main_category=main_category, **validated_data)
        return sub_category

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    main_category = MainCategorySerializer(read_only=True)
    sub_category = SubCategorySerializer(read_only=True)
    main_category_id = serializers.PrimaryKeyRelatedField(
        queryset=MainCategory.objects.all(), write_only=True
    )
    sub_category_id = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all(), write_only=True
    )

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'image', 'created_at', 
                   'main_category', 'main_category_id', 
                   'sub_category', 'sub_category_id']

    def create(self, validated_data):
        main_category = validated_data.pop('main_category_id')
        sub_category = validated_data.pop('sub_category_id')
        course = Course.objects.create(
            main_category=main_category,
            sub_category=sub_category,
            **validated_data
        )
        return course




