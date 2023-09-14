#!/usr/bin/python3
"""This module defines a script that lists all states starting with N"""
import MySQLdb
import sys


def get_states_N(username, password, name):
    """This function lists all states starting with N"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=name
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    get_states_N(username, password, name)
