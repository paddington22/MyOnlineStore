from django.shortcuts import render
from rest_framework import generics
from rest_framework import pagination
from api.serializers import ProductSerializer
from products.models import Product


# Create your views here.
class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
