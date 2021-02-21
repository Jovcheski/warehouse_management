from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    category = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    product = models.CharField(max_length=256)
    price = models.FloatField()
    warranty = models.IntegerField()

    def __str__(self):
        return f'{self.category} {self.product} {self.price}'

    def get_absolute_url(self):
        return reverse('warehouse_m:index')



