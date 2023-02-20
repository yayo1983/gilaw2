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


class CategoryN(models.Model):
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    users = models.ManyToManyField(User)
    class Meta:
        db_table = "api_categoryn"

    def __str__(self):
        return self.category


class TypeN(models.Model):
    type = models.CharField(
        max_length=70,
        choices=[x.value for x in TypeNotification],
        default=TypeNotification.get_value('sms'))
    
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

    @property
    def full_name_user(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def email(self):
        return self.user.email

    @property
    def phone(self):
        return self.user.phone

    @property
    def message(self):
        return self.content_object.message

    @property
    def category(self):
        return self.content_object.category


class SMSNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notifications = GenericRelation(Notification)


class EmailNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notifications = GenericRelation(Notification)


class PushNotification(models.Model):
    message = models.TextField(null=False, verbose_name="message")
    category = models.CharField(
        max_length=70,
        choices=[x.value for x in Category],
        default=Category.get_value('sports'))
    created_at = models.DateTimeField(auto_now_add=True)
    notifications = GenericRelation(Notification)
