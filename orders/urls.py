from django.urls import path

from .views import OrderCreateView, OrderListView, OrderDetailListView

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:pk>', OrderDetailListView.as_view(), name='order-detail'),
    path('confirm/', OrderCreateView.as_view(), name='order-create'),
]