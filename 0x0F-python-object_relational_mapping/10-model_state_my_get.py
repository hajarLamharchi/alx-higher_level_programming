#!/usr/bin/python3
"""This module prints the state with the name passed as argument"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session


def print_state(username, password, name, state):
    """This function prints the state passed as argument"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = (
            session.query(State)
            .filter(State.name == state)
            .first()
        )
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state = sys.argv[4]
    print_state(username, password, name, state)
