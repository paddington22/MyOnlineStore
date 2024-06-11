from django.contrib import admin

from orders.models import Product, Category, Client

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Client)
