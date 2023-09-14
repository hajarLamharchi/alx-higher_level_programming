#!/usr/bin/python3
"""This module defines a function that lists all cities of a state"""
import MySQLdb
import sys


def get_cities_by_state(username, password, name, state):
    """This function lists all cities of a state"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=name
        )
    cur = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id
    """
    cur.execute(query, (state, ))
    rows = cur.fetchall()
    list1 = []
    for row in rows:
        list1.append(row[0])
    print(", ".join(list1))

    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state = sys.argv[4]
    get_cities_by_state(username, password, name, state)
