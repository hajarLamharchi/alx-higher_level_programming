#!/usr/bin/python3
"""This script adds a new state to the database"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session


def add_state(username, password, name):
    """This function adds the state Louisiana to the database"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    add_state(username, password, name)
