from django.urls import path

from .views import OrderCreateView

urlpatterns = [
    path('confirm/', OrderCreateView.as_view(), name='order-create'),
]