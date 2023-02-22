import graphene
from .models import Notification
from graphene_django import DjangoObjectType
from .serializers import NotificationSerializer


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


class CreateNotification(graphene.Mutation):
    id = graphene.Int()
    category = graphene.String()
    message = graphene.String()

    class Arguments:
        category = graphene.String()
        message = graphene.String()

    def mutate(self, info, category, message):
        serializer = NotificationSerializer()
        return serializer.save_notification(message, category)


class MutationNotification(graphene.ObjectType):
    create_notification = CreateNotification.Field()


schema = graphene.Schema(query=Query, mutation=MutationNotification)
