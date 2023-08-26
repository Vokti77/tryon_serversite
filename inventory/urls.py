
from django.urls import path
from .views import CategoryListCreateView, ClothesDetailView, ClothesListView, CategoryRetrieveUpdateDeleteView, SubCategoryListCreateView, SubCategoryRetrieveUpdateDeleteView, ClothesViewAPI

urlpatterns = [
    
    path('categories', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>', CategoryRetrieveUpdateDeleteView.as_view(), name='category-detail'),
    path('subcategories', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>', SubCategoryRetrieveUpdateDeleteView.as_view(), name='subcategory-detail'),
    path('clothes/', ClothesViewAPI.as_view(), name='clothes'),
    path('clothes_list', ClothesListView.as_view(), name='clothes-list'),
    path('clothes/<int:pk>', ClothesDetailView.as_view(), name='clothes-detail'),
  
]
