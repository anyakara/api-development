from sqlalchemy import Column, Integer, String, relationship, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""This is an example."""
class SomeClass(Base):
    __tablename__ = 'some_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String)
    first_name = Column(String)
    email = Column(String, unique=True, index=True)
    todos = relationship("TODO", back_populates="owner", cascade="all, delete-orphan")
