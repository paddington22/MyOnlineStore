from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    image = models.ImageField(upload_to='static/products/', null=True, blank=True, verbose_name='Изображение')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    unit_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')


    def __str__(self):
        return self.name

@receiver(post_save, sender=Product)
def update_stock(sender, instance, **kwargs):
    ProductInStock.objects.create(product=instance, quantity=0)


class ProductInStock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{Product.objects.get(id=self.product)}'


class Category(models.Model):
   name = models.CharField(max_length=255, verbose_name='Название')
   description = models.TextField(null=True, blank=True, verbose_name='Описание')

   def __str__(self):
     return self.name







