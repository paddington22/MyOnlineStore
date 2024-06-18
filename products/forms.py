from django import forms
from users.models import ProductInBasket

class ProductInBasketCreateForm(forms.ModelForm):
    class Meta:
        model = ProductInBasket
        fields = ['quantity']

