from enum import Enum
from django.db import models
from users.models import User
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
        db_table = "api_type_notification"

    def __str__(self):
        return self.type


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content_object = GenericForeignKey()
    object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

class SMSNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notifications = GenericRelation(Notification)
   # usern = models.ForeignKey(UserNotification, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class EmailNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notifications = GenericRelation(Notification)
    # usern = models.ForeignKey(UserNotification, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class PushNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notifications = GenericRelation(Notification)
    # usern = models.ForeignKey(UserNotification, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


  
# class TypeNUser(models.Model):
#     usern = models.ForeignKey(UserNotification, on_delete = models.CASCADE, related_name = "type")
#     typen = models.ForeignKey(TypeN, on_delete = models.CASCADE, related_name = "usernotification")
