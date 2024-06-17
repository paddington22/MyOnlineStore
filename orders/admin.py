from django.contrib import admin

from orders.models import  OrderStatus, Order, ProductInOrder


# Register your models here.
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(ProductInOrder)

