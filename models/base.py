from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def set_meta(engine):
    Base.metadata.create_all(engine)
