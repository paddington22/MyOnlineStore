from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy, reverse

from .forms import OrderCreateForm
from products.models import Product
from users.models import ProductInBasket
from .models import ProductInOrder, Order


# Create your views here.
class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'orders/order_confirm.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('profile')

    def get_summary(self):
        summary = 0
        products_in_basket = self.get_queryset()

        for product_in_basket in products_in_basket:
            product = Product.objects.get(pk=product_in_basket.product_id)
            temp_summary = product.unit_price * product_in_basket.quantity
            summary += temp_summary

        return summary

    def get_queryset(self):
        return ProductInBasket.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_in_basket = self.get_queryset()
        result = []

        for product_in_basket in products_in_basket:
            product = Product.objects.get(pk=product_in_basket.product_id)
            result.append([product_in_basket, product.unit_price, product.image])

        context['products_in_basket_info'] = result
        context['summary'] = self.get_summary()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.summary = self.get_summary()
        self.object.user_id = self.request.user.id
        self.object.save()

        products_in_basket = self.get_queryset()
        for product_in_basket in products_in_basket:
            ProductInOrder.objects.create(unit_price=Product.objects.get(id=product_in_basket.product_id).unit_price,
                                          quantity=product_in_basket.quantity,
                                          order_id=self.object.id,
                                          product_id=product_in_basket.product_id)
            ProductInBasket.objects.filter(id=product_in_basket.id).delete()

        return super(OrderCreateView, self).form_valid(form)


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'order_list.html'
    model = Order
    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.id)






