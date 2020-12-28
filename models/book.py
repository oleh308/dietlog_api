from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, Unicode, String, Text

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(256), index=True, nullable=False)
    description = Column(Text, nullable=False)
    year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '' % self.title % self.description % self.year % self.author_id
