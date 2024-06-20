from django.urls import path
from .views import ProfileListView, ProfileUpdateView, ProductInBasketItemUpdateView, NewOrderCreateView, \
    ProductInBasketItemDeleteView

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='profile'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/basket/',NewOrderCreateView.as_view() , name='basket'),
    path('profile/basket/<int:pk>/update/', ProductInBasketItemUpdateView.as_view(), name='basket-update-item'),
    path('profile/basket/<int:pk>/delete/', ProductInBasketItemDeleteView.as_view(), name='basket-delete-item'),
]
