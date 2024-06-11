from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products_image/')
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
   name = models.CharField(max_length=255)
   description = models.TextField(null=True, blank=True)

   def __str__(self):
     return self.name

