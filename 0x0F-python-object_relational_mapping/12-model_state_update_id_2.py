#!/usr/bin/python3
"""This script changes the name of a state"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session


def update_state(username, password, name):
    """This function updates a state from the table"""
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(username,
                                      password,
                                      name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = (
            session.query(State)
            .filter(State.id == 2)
            .first()
        )

    state.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    update_state(username, password, name)
