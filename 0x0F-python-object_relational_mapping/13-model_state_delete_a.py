#!/usr/bin/python3
"""This script deletes states from the database"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session


def delete_states(username, password, name):
    """This function deletes dtates from the database"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .all()
        )
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    delete_states(username, password, name)
