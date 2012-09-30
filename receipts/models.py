from django.db import models
from products.models import Product
from members.models import Member


# Create your models here.
class Receipt(models.Model):
    code = models.IntegerField(blank=True, null=True)
    products = models.ManyToManyField(Product, related_name='receipts')
    created_at = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member, blank=True, null=True)
