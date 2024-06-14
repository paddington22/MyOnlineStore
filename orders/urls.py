from django.urls import path
from .views import ProductListView, ProductDetailListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailListView.as_view(), name='product-detail'),
    #path('add_to_cart/', add_to_cart, name='add-to-cart'),
]