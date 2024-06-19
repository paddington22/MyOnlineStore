from django.urls import path
from .views import ProfileListView, ProfileUpdateView, ProductInBasketUpdateView, NewOrderCreateView

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='profile'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/basket/',NewOrderCreateView.as_view() , name='basket'),
    path('profile/basket/<int:pk>', ProductInBasketUpdateView.as_view(), name='basket-update')
]
