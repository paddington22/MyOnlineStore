from django.urls import path

from .views import OrderCreateView, OrderListView

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('confirm/', OrderCreateView.as_view(), name='order-create'),
]