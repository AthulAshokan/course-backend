from django.urls import path
from . import views

app_name ='course_api'

urlpatterns = [
    path('category/create/', views.category_create, name='main-category-create'),
    path('category/list/', views.category_list, name='main-category-list'),
    path('category/<int:pk>/update/', views.category_update, name = 'main-category-update'),
    path('catgory/<int:pk>/delete/', views.category_delete, name='main-category-delete'),

    path('subcategory/create/' ,views.create_subcategory, name='sub-category-create'),
    path('subcategory/list/', views.subcategory_list, name='sub-category-list'),
    path('subcategory/<int:pk>/update/', views.subcategory_update, name='sub-category-update'),
    path('subcategory/<int:pk>/delete/', views.subcategory_delete, name='sub-category-delete'),
]



