import graphene
from schemas.book import BookObject
from schemas.user import UserObject
from graphene_sqlalchemy import SQLAlchemyConnectionField

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_books = SQLAlchemyConnectionField(BookObject)
    all_users = SQLAlchemyConnectionField(UserObject)

schema = graphene.Schema(query=Query)
