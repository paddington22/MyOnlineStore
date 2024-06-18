from django.urls import path
from .views import ProductListView, ProductInBasketCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductInBasketCreateView.as_view(), name='product-detail-list'),
]