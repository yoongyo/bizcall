from contact.schema import Query as PostQuery
from message.schema import Query as MessageQuery

import graphene


class Query(PostQuery, MessageQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
