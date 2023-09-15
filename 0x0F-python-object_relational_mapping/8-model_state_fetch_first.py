#!/usr/bin/python3
"""This module defines a script that prints the first state"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session


def first_state(username, password, name):
    """This function prints the first state"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    first_state(username, password, name)
