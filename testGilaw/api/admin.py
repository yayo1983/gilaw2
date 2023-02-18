from django.contrib import admin

# Register your models here.
from .models import SMSNotification, EmailNotification, PushNotification


admin.site.register(SMSNotification)
admin.site.register(EmailNotification)
admin.site.register(PushNotification)
# admin.site.register(UserNotification)

