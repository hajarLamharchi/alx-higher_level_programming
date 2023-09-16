#!/usr/bin/python3
"""This module lists all city objects from the database"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def list_city(username, password, name):
    """This function lists all city objects from the database"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = (
            session.query(City)
            .join(State)
            .order_by(City.id)
            .all()
        )
    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    list_city(username, password, name)
