#!/usr/bin/python3
"""This module lists all states and corresponding cities"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def list_states_cities(username, password, name):
    """This function lists all states and corresponding cities"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = (
            session.query(State)
            .order_by(State.id)
            .all()
        )

    for state in query:
        print("{}: {}".format(state.id, state.name))
        cities = state.cities
        for city in cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    list_states_cities(username, password, name)
