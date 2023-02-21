import graphene 
from .models import Notification
from graphene_django import DjangoObjectType

class NotificationG(DjangoObjectType):
    class Meta:
        model = Notification
        fields = '__all__'

class Query(graphene.ObjectType):
    all_logs = graphene.List(NotificationG)

    def resolve_all_logs(root, info):
        return Notification.objects.all()
    
schema = graphene.Schema(query=Query)