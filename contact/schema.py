import graphene
from graphene_django.types import DjangoObjectType
from .models import Contact, Item


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class Query(graphene.AbstractType):
    all_contact = graphene.List(ContactType)

    all_item = graphene.List(ItemType)

    def resolve_all_contacts(self, context, **kwargs):
        return Contact.objects.all()

    def resolve_all_item(self, context, **kwargs):
        return Item.objects.all()
