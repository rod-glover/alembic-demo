from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True, nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    login = Column(String(64), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column('address_id', Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    street = Column(String(128), nullable=False)
    city = Column(String(64), nullable=False)
    province = Column(String(32), nullable=False)
    postal_code = Column(String(6))
