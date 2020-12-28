import graphene
from models.user import User
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = User
       interfaces = (graphene.relay.Node, )
