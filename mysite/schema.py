from contact.schema import Query as PostQuery
from message.schema import Query as MessageQuery
from accounts.schema import Query as UserQuery
import graphene


class Query(PostQuery, MessageQuery, UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
