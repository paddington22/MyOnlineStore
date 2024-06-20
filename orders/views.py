from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy, reverse

from .forms import OrderCreateForm
from products.models import Product
from users.models import ProductInBasket


# Create your views here.
class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'orders/order_confirm.html'
    form_class = OrderCreateForm

    def get_queryset(self):
        return ProductInBasket.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        summary = 0
        context = super().get_context_data(**kwargs)
        products_in_basket = ProductInBasket.objects.filter(user_id=self.request.user.id)
        result = []

        for product_in_basket in products_in_basket:
            product = Product.objects.get(pk=product_in_basket.product_id)
            temp_summary = product.unit_price * product_in_basket.quantity
            result.append([product_in_basket, product.unit_price, product.image])
            summary += temp_summary

        context['products_in_basket_info'] = result
        context['summary'] = summary
        return context



