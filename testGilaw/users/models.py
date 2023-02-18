from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.IntegerField(null=False, blank=True, verbose_name="Phone")
    name = models.CharField(max_length=250, null=False,
                            blank=True, verbose_name="name")

    def __str__(self):
        return self.username
