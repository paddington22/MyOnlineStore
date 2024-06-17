from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, ProductInBasket

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ProductInBasket)
