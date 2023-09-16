#!/usr/bin/python3
"""This script prints all cities"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def print_cities(username, password, name):
    """This function prints all the cities from the data base"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    cities = (
            session.query(City, State)
            .join(City, State.id == City.state_id)
            .order_by(City.id)
            .all()
        )
    for city, state in cities:
        print("{}: ({}) {}".format(state.name,
                                   city.id,
                                   city.name))
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    print_cities(username, password, name)
