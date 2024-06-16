from datetime import datetime
from users.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class ProfileManager(models.Manager):

    def for_user(self, user):
        return self.get_queryset().filter(user=user)

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    image = models.ImageField(upload_to='static/products/', null=True, blank=True, verbose_name='Изображение')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    unit_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')


    def __str__(self):
        return self.name



class ProductInStock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{Product.objects.get(id=self.product_id)}'

@receiver(post_save, sender=Product)
def update_stock(sender, instance, **kwargs):
    ProductInStock.objects.create(product=instance, quantity=0)



class Category(models.Model):
   name = models.CharField(max_length=255, verbose_name='Название')
   description = models.TextField(null=True, blank=True, verbose_name='Описание')

   def __str__(self):
     return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия')
    patronymic_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Отчество')
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    email = models.EmailField(null=True, blank=True, verbose_name='Электронная почта')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    objects = ProfileManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

@receiver(post_save, sender=User)
def update_client(sender, instance, **kwargs):
    Client.objects.create(user=instance)


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
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент')
    order_status = models.ForeignKey(to='OrderStatus',
                                        on_delete=models.PROTECT,
                                        default=OrderStatus.get_default_pk,
                                        verbose_name='Cтатус заказа')
    summary = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма')
    order_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата и время заказа')
    products = models.ManyToManyField('Product', through='ProductInOrder')

    def __str__(self):
        return f'Заказ № {self.id} (заказчик: {self.client_id})'


class ProductInBasket(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    basket = models.ForeignKey('ShoppingBasket', on_delete=models.CASCADE, verbose_name='Корзина')
    quantity = models.IntegerField(verbose_name='Количество')


class ShoppingBasket(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент')
    products = models.ManyToManyField('Product', through='ProductInBasket')

    def __str__(self):
        return f'{self.client.first_name} {self.client.last_name}'

@receiver(post_save, sender=Client)
def update_basket(sender, instance, **kwargs):
    ShoppingBasket.objects.create(client=instance)



class ProductInOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='№ заказа')
    unit_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')


#class PurchaseHistory(models.Model):
#    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент')
