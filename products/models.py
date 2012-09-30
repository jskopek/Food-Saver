from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    expires_at = models.DateField(blank=True, null=True)
    perishable = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
