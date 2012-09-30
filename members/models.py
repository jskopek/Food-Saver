from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from datetime import date


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    phone_number = models.CharField(max_length=255)

    def get_products(self):
        perishables = list(self.get_perishables())
        non_perishables = list(Product.objects.filter(expires_at__isnull=True, receipt__member=self))
        return perishables + non_perishables

    def get_perishables(self):
        return Product.objects.filter(expires_at__gte=date.today(), receipt__member=self)

    def __unicode__(self):
        return self.phone_number
