from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from products.models import Product


# Create your models here.
class ProfileManager(UserManager):

    def for_user(self, user):
        return self.get_queryset().filter(username=user)[0]


class User(AbstractUser):
    product = models.ManyToManyField(Product, through="ProductInBasket")

    objects = ProfileManager()

    def __str__(self):
        return self.username


class ProductInBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return self.product.name
