from django.contrib.auth.models import AbstractUser
from django.db import models

from products.models import Product


# Create your models here.
class ProfileManager(models.Manager):

    def for_user(self, user):
        return self.get_queryset().filter(user=user)


class User(AbstractUser):
    product = models.ManyToManyField(Product, through="ProductInBasket")

    objects = ProfileManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ProductInBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    quantity = models.IntegerField(verbose_name='Количество')

