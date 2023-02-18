from users.models import User
from abc import ABC, abstractmethod

from .models import SMSNotification, EmailNotification, PushNotification


class AbstractFactoryModel(ABC):

    @abstractmethod
    def create_sms_notification_model(self):
        pass

    @abstractmethod
    def create_email_notification_model(self):
        pass
    
    @abstractmethod
    def create_push_notification_model(self):
        pass


class FactoryModel(AbstractFactoryModel):

    def create_sms_notification_model(self):
        return SMSNotification()

    def create_email_notification_model(self):
        return EmailNotification()
    
    def create_push_notification_model(self):
        return PushNotification()
    
    def create_notification(self, category):
        if category is 'Finance':
            return User.objects.get(username='yasserfinance'), self.create_email_notification_model()
        elif category is 'Movies':
            return User.objects.get(username='yassermovies'), self.create_push_notification_model()
        else:
            return User.objects.get(username='yassersport'), self.create_sms_notification_model()
