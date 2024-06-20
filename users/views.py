from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView, FormView, CreateView, DeleteView

from products.forms import ProductInBasketCreateForm
from products.models import Product
from .models import User, ProductInBasket


# Create your views here.
class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'profile/profile.html'
    def get_queryset(self):
        return User.objects.for_user(self.request.user)

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    client = Client.objects.for_user(self.request.user).get(pk=13)
    #    context['client'] = client
    #    print(client)
    #    return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profile/profile_form.html'
    fields = ['first_name', 'last_name', 'email']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование информации профиля"
        context['client'] = self.object.pk
        return context

    def get_success_url(self):
        return reverse('profile')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form


class NewOrderCreateView(LoginRequiredMixin, FormView):
    template_name = 'profile/basket.html'

    def get_form(self, form_class=ProductInBasketCreateForm):
        form = super().get_form(form_class)
        return form

    def get_context_data(self, **kwargs):
        summary = 0
        context = super().get_context_data(**kwargs)
        products_in_basket = ProductInBasket.objects.filter(user=self.request.user)
        products_list = Product.objects.all()
        result = []
        for product in products_list:
            for product_in_basket in products_in_basket:
                if product.id == product_in_basket.product_id:
                    temp_summary = product.unit_price * product_in_basket.quantity
                    result.append([product_in_basket, product.unit_price, temp_summary, product.image])
                    summary += temp_summary

        context['products_in_basket_info'] = result
        context['summary'] = summary
        return context


class ProductInBasketItemUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductInBasket
    template_name = 'basket_update.html'
    form_class = ProductInBasketCreateForm
    success_url = reverse_lazy('basket')

class ProductInBasketItemDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductInBasket
    success_url = reverse_lazy('basket')
    template_name = 'profile/basket_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_in_basket = ProductInBasket.objects.get(pk=self.kwargs['pk'])
        quantity = product_in_basket.quantity
        product = Product.objects.get(pk=product_in_basket.product_id)
        context['product'] = product
        context['quantity'] = quantity
        return context
