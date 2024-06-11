from django.contrib import admin

from orders.models import Product, Category, Client, OrderStatus, Order, ProductInStock

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(ProductInStock)

