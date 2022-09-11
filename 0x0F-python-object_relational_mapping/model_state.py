#!/usr/bin/python3

"""Definition of a class State with module SQLAlchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

""""Base to inherit from"""
Base = declarative_base()


class State(Base):
    """"A class with an instance from Base
    args:
        __table__: initializes the table name as state
        id: (int) unique identifer of the table
        name: (str)
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullabe=False, primary_key=True)
    name = Column(String(128), nullable=False)
