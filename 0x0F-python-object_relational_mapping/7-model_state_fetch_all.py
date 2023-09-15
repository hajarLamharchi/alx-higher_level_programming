#!/usr/bin/python3
"""This script lists all the states from the database"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session


def list_states(username, password, name):
    """This function lists all the states"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    list_states(username, password, name)
