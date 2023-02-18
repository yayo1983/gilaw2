from .models import Notification
from django.db import transaction
from rest_framework import serializers
from .abstract_factory_model import FactoryModel

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    @transaction.atomic()
    def save_notification(self, message, category):
        try:
            factory = FactoryModel()
            user, auxNotification = factory.create_notification(category)
            auxNotification.message = message
            auxNotification.category = category
            auxNotification.save()
            Notification.objects.create(user=user, content_object=auxNotification)
            return True
        except:
            return False


    
