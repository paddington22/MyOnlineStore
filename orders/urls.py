from django.urls import path
from .views import product_detail, ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    #path('add_to_cart/', add_to_cart, name='add-to-cart'),
]