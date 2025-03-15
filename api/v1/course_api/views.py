from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from courses.models import MainCategory
from .serializers import MainCategorySerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from courses.models import SubCategory
from .serializers import SubCategorySerializer

#### main_category section
#create main_category
@api_view(['POST'])
@permission_classes([AllowAny])
def category_create(request): 
        serializer = MainCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#get all main_categories    
@api_view(['GET'])
@permission_classes([AllowAny])
def category_list(request):
    categories = MainCategory.objects.all()
    serializer = MainCategorySerializer(categories, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#update main_category
@api_view(['PUT'])
@permission_classes([AllowAny])
def category_update(request, pk):
     try:
          category = MainCategory.objects.get(pk=pk)
     except MainCategory.DoesNotExist:
          return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

     serializer = MainCategorySerializer(category, data = request.data)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
     
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete main_category
@api_view(['DELETE'])
@permission_classes([AllowAny])
def category_delete(request,pk):
     try:
          category = MainCategory.objects.get(pk=pk)
     except MainCategory.DoesNotExist:
          return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
     
     category.delete()
     return Response({'detail': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

#### subcategory_section

@api_view(['POST'])
@permission_classes([AllowAny])
def create_subcategory(request):
    print(request.data,"...............")
    serializer = SubCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([AllowAny])
def subcategory_update(request, pk):
    print(request.data,"...............")
    try:
        subcategory = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        return Response({'error': 'Subcategory not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = SubCategorySerializer(subcategory, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def subcategory_delete(request, pk):
    try:
        subcategory = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        return Response({'error': 'Subcategory not found'}, status=status.HTTP_404_NOT_FOUND)

    subcategory.delete()
    return Response({'detail': 'Subcategory deleted successfully'}, status=status.HTTP_204_NO_CONTENT)






