from django.db import models
from products.models import Product


# Create your models here.
class Receipt(models.Model):
    code = models.IntegerField(blank=True, null=True)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
