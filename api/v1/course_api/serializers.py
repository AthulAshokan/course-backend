from rest_framework import serializers
from courses.models import MainCategory, SubCategory

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
