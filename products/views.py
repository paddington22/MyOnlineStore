from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Product
# Create your views here.


class ProductListView(LoginRequiredMixin, ListView):
    #login_url = reverse_lazy('account_login')
    #template_name = 'orders/product_list.html'

    def get_queryset(self):
        return Product.objects.all().order_by('name')


class ProductDetailListView(LoginRequiredMixin, ListView):
    template_name = 'products/product_detail_list.html'

    def get_queryset(self):
        return Product.objects.all().filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['product'] = product
        return context