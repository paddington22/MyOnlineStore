from django.urls import path

from api.views import ProductListApiView

urlpatterns = [
    path('products/', ProductListApiView.as_view()),
]