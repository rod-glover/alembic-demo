from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())
metadata = Base.metadata


class User(Base):
    id = Column('user_id', Integer, primary_key=True, nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    login = Column(String(64), nullable=False)
