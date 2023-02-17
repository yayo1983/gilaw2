from enum import Enum
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey


class Notification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    created_at = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=10, choices=[(
    #     tag.name, tag.value) for tag in Category], verbose_name="Category", null=True, default='S')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


    class Meta:
        db_table = "notification"

    def __str__(self):
        return self.message
    

class SMSNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    created_at = models.DateTimeField(auto_now_add=True)
    notification = GenericRelation(Notification)

    def __str__(self):
        return self.message


class EmailNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    created_at = models.DateTimeField(auto_now_add=True)
    notification = GenericRelation(Notification)

    def __str__(self):
        return self.message
    

class PushNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    created_at = models.DateTimeField(auto_now_add=True)
    notification = GenericRelation(Notification)

    def __str__(self):
        return self.message
    
    
class UserNotification(models.Model):
    class Category(Enum):
        S = "Sports"
        F = "Finance"
        M = "Movies"

        @classmethod
        def choices(cls):
            return [(item.value, item.name) for item in cls]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=False,
                            blank=True, verbose_name="name")
    phone = models.IntegerField(null=False, blank=True, verbose_name="Phone")
    channels = models.ForeignKey(Notification, on_delete=models.CASCADE)
    subscribed =  models.CharField(max_length=2, choices=[x.value for x in Category])
