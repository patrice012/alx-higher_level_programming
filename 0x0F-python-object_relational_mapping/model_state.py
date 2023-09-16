#!/usr/bin/python3
"""
Python module that contains class definition of a State
and an instance Base = declarative_base()


State class:
    -- inherits from Base Tips
    -- links to the MySQL table states
    -- class attribute id that represents a
    column of an auto-generated, unique -integer,
    can't be null and is a primary key
    -- class attribute name that represents a
    column of a string with maximum 128
    characters and can't be null
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class definition of states database table

    __tablename__(str): name of database table to map to
    id(sqlalchemy.Integer): The state's id.
    name(sqlalchemy.String): The state's name.
    """

    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
