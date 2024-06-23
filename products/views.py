from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from .models import Product
from users.models import ProductInBasket, User
from django.urls import reverse
from .forms import ProductInBasketCreateForm


# Create your views here.
class ProductListView(ListView):
    #login_url = reverse_lazy('account_login')
    #template_name = 'orders/product_list.html'

    def get_queryset(self):
        return Product.objects.all().order_by('name')


class ProductInBasketCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductInBasketCreateForm
    template_name = 'products/product_detail_list.html'

    def get_queryset(self):
        return Product.objects.all().filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('product-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        query = ProductInBasket.objects.filter(user_id=self.request.user.id).filter(product_id=product.id)

        if not query.exists():
            context['product_in_basket_id'] = query
        else:
            product_in_basket_id = ProductInBasket.objects.filter(user_id=self.request.user.id).get(product_id=product.id).id
            context['product_in_basket_id'] = product_in_basket_id

        context['product'] = product
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = Product.objects.get(pk=self.kwargs['pk'])
        self.object.user = self.request.user
        self.object.save()
        return super(ProductInBasketCreateView, self).form_valid(form)





