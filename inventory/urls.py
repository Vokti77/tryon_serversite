
from django.conf.urls import url
from inventory import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDeleteView, SubCategoryListCreateView, SubCategoryRetrieveUpdateDeleteView, UploadView, UploadViewAPI, AttachmentListView

urlpatterns = [
    path('upload/', views.upload_images, name='upload_images'),
    # path('output/', views.output, name='output'),
    path('categories', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>', CategoryRetrieveUpdateDeleteView.as_view(), name='category-detail'),
    path('subcategories', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>', SubCategoryRetrieveUpdateDeleteView.as_view(), name='subcategory-detail'),
    path('mulup', UploadView.as_view(), name="mulup"),
    path('upapi/', UploadViewAPI.as_view(), name='upapi'),
     path('attachments/', AttachmentListView.as_view(), name='attachment-list'),

]


# urlpatterns=[
#     url(r'^category$',views.categoryApi),
#     url(r'^category/([0-9]+)$',views.categoryApi),
# ]