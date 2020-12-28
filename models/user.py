from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Unicode, String, Text

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    books = relationship('Book', backref='author')

    def __init__(self, username, email):
      self.username = username
      self.email = email

    def __repr__(self):
        return '' % self.id
