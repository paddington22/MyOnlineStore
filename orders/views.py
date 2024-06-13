from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product, 'image': f'/{product.image}'}
    return render(request, 'products/product_detail.html', context)

