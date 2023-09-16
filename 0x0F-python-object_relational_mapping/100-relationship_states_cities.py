#!/usr/bin/python3
"""This module creates the State 'California' with
    the City 'San Francisco' from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def create_state_city(username, password, name):
    """This function creates the State 'California' with
        the City 'San Francisco' from the database
    """
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_city = City(name='San Francisco')
    new_state = State(name='California', cities=[new_city])

    session.add(new_city)
    session.add(new_state)
    session.commit()

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    create_state_city(username, password, name)
