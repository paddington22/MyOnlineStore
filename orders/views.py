from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Product


# Create your views here.
class ProductListView(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        return Product.objects.all()


#class ProductDetailView(ListView):
#    template_name = 'products/product_detail.html'


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product, 'image': f'/{product.image}'}
    return render(request, 'products/product_detail.html', context)

