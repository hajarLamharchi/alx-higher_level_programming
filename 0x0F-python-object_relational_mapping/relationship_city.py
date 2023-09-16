#!/usr/bin/python3
"""This module defines the class city"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """This class defines a city with:
    Attributes:
        id: unique integer, can't be null
        name: string, can't be null
        state_id: integer, can't be null
    """
    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
