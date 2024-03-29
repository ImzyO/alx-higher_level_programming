#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,\
            passwd=argv[2], db=argv[3])
    with db.cursor() as typed:
        typed.execute("""SELECT cities.id, cities.name FROM JOIN states ON cities.state_id = states.id states.name LIKE BINARY %(state_name)s ORDER BY cities.id ASC""", {'state_name': argv[4]})

        rows = typed.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
