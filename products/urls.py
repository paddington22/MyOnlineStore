from django.urls import path
from .views import ProductListView, ProductDetailListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailListView.as_view(), name='product-detail-list'),
]