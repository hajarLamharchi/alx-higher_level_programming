#!/usr/bin/python3
"""This module defines the function get_state_name()"""
import MySQLdb
import sys


def get_state_name(username, password, name, state):
    """This function displays all values of state that matches the argument"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=name
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id",
                (state, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state = sys.argv[4]
    get_state_name(username, password, name, state)
