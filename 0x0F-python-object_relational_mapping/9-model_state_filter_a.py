#!/usr/bin/python3
"""This module lists the states that contains the letter a"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session


def a_states(username, password, name):
    """This function lists states containing the letter a"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id)
            .all()
        )
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    a_states(username, password, name)
