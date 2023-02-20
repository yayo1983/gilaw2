from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    phone = models.IntegerField(null=True, blank=True, verbose_name="Phone")

    @property
    def channels(self):
        return self.type_notification_set.all()
    
    @property
    def subscribed(self):
        return self.category_set.all()
    
    def __str__(self):
        return self.username
    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

 
