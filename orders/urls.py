from django.urls import path
from .views import ProductListView, ProductDetailListView, ProfileListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailListView.as_view(), name='product-detail'),
    path('accounts/profile/', ProfileListView.as_view(), name='profile'),
    #path('add_to_cart/', add_to_cart, name='add-to-cart'),
]