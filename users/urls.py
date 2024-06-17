from django.urls import path
from .views import ProfileListView, ProfileUpdateView

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='profile'),
    path('profile/<int:pk>', ProfileUpdateView.as_view(), name='profile-update')
]