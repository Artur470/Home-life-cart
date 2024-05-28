from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('list/', ProductListCreateView.as_view(), name='product-list'),
    path('list/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('attributes/', AttributeListCreateView.as_view(), name='attribute-list'),
    path('attributes/<int:pk>/', AttributeDetailView.as_view(), name='attribute-detail'),
]
