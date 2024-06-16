from django.urls import path
from .views import ProductListView, ProductDetailListView, ProfileListView, ProfileUpdateView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailListView.as_view(), name='product-detail-list'),
    path('accounts/profile/', ProfileListView.as_view(), name='profile'),
    path('accounts/profile/<int:pk>', ProfileUpdateView.as_view(), name='profile-update')
    #path('add_to_cart/', add_to_cart, name='add-to-cart'),
]