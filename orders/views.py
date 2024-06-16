from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from .models import Product, Client
from django.urls import reverse_lazy, reverse


# Create your views here.
class ProductListView(LoginRequiredMixin, ListView):
    #login_url = reverse_lazy('account_login')
    #template_name = 'orders/product_list.html'

    def get_queryset(self):
        return Product.objects.all().order_by('name')


class ProductDetailListView(LoginRequiredMixin, ListView):
    template_name = 'orders/product_detail_list.html'

    def get_queryset(self):
        return Product.objects.all().filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['product'] = product
        return context

class ProfileListView(LoginRequiredMixin, ListView):
    template_name = 'profile/profile.html'
    def get_queryset(self):
        return Client.objects.for_user(self.request.user)[0]

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    client = Client.objects.for_user(self.request.user).get(pk=13)
    #    context['client'] = client
    #    print(client)
    #    return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'profile/profile_form.html'
    fields = ['first_name', 'last_name', 'patronymic_name', 'phone_number', 'email']

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


