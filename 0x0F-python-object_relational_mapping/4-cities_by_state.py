#!/usr/bin/python3
"""This module defines the function that lists all cities from a database"""
import MySQLdb
import sys


def get_cities(username, password, name):
    """This function lists all cities from a database"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=name
        )
    cur = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON states.id = cities.state_id
    ORDER BY cities.id
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    get_cities(username, password, name)
