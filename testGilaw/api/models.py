from enum import Enum
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey


class Category(Enum):
    sports = ('Sports', 'Sports')
    finance = ('Finance', 'Finance ')
    movies = ('Movies', 'Movies')

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]

    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]
    
    
class TypeNotification(Enum):
    sms = ('SMS', 'SMS')
    email = ('Email', 'Email ')
    pushNotification = ('Push Notification', 'Push Notification')

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]

    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]


class TypeN(models.Model):
    type = models.CharField(
        max_length=70,
        choices=[x.value for x in TypeNotification],
        default=TypeNotification.get_value('sms'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "type_notification"

    def __str__(self):
        return self.type


class Notification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
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
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notification = GenericRelation(Notification)

    def __str__(self):
        return self.message


class EmailNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notification = GenericRelation(Notification)

    def __str__(self):
        return self.message


class PushNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notification = GenericRelation(Notification)

    def __str__(self):
        return self.message


class UserNotification(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=False, blank=True, verbose_name="Phone")
    name = models.CharField(max_length=250, null=False,
                            blank=True, verbose_name="name")
    channels = models.ForeignKey(Notification, on_delete=models.CASCADE)
    subscribed = models.CharField(max_length=50, choices=[
        x.value for x in Category], default=Category.get_value('sports'))
   
    
class TypeNUser(models.Model):
    usern = models.ForeignKey(UserNotification, on_delete = models.CASCADE, related_name = "type")
    typen = models.ForeignKey(TypeN, on_delete = models.CASCADE, related_name = "usernotification")
