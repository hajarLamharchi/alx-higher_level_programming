#!/usr/bin/python3
"""This module defines the class definition of a state"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class defines a state with:
    Attributes:
    id: unique integer, can't be null
    name: string, can't be null
    """
    __tablename__ = "states"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
