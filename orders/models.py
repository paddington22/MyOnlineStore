from datetime import datetime
from django.db import models
from users.models import User
from products.models import Product



# Create your models here.
class OrderStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    @classmethod
    def get_default_pk(cls):
        order_status, created = cls.objects.get_or_create(
            name='В обработке',
            defaults=dict(description='Ожидайте подтверждения'),
        )
        return order_status.pk

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    order_status = models.ForeignKey(to='OrderStatus', on_delete=models.PROTECT, default=OrderStatus.get_default_pk, verbose_name='Cтатус заказа')
    summary = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма')
    order_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата и время заказа')
    products = models.ManyToManyField(Product, through="ProductInOrder")
    comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='Комментарий к заказу')
    def __str__(self):
        return f'Заказ № {self.id} (заказчик: {self.client_id})'


class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Товар')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='№ заказа')
    unit_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')










