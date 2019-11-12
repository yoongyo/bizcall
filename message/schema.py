import graphene
from graphene_django.types import DjangoObjectType
from .models import Message


class MessageType(DjangoObjectType):
    class Meta:
        model = Message


class Query(graphene.AbstractType):
    all_message = graphene.List(MessageType)

    def resolve_all_messages(self, context, **kwargs):
        return Message.objects.all()
