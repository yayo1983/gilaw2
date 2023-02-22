import graphene 
from .models import Notification
from graphene_django import DjangoObjectType

class NotificationG(DjangoObjectType):
    full_name_user = graphene.String(source='full_name_user')
    email = graphene.String(source='email')
    phone = graphene.String(source='phone')
    message = graphene.String(source='message')
    category = graphene.String(source='category')
    class Meta:
        model = Notification
        fields = ('id', 'created_at')

class Query(graphene.ObjectType):
    all_logs = graphene.List(NotificationG)

    def resolve_all_logs(root, info):
        return Notification.objects.all().order_by('-created_at')
    
schema = graphene.Schema(query=Query)