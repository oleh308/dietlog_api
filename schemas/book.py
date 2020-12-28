import graphene
from models.book import Book
from graphene_sqlalchemy import SQLAlchemyObjectType

class BookObject(SQLAlchemyObjectType):
   class Meta:
       model = Book
       interfaces = (graphene.relay.Node, )
