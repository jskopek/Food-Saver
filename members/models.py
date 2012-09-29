from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    phone_number = models.CharField(max_length=255)

    def __unicode__(self):
        return self.phone_number
