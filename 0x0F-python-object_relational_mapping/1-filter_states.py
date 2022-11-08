#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:"""
""" script should take 3 arguments: mysql username, mysql password and database name"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,\
            passwd=argv[2], db=argv[3])
    typed = db.cursor()
    typed.execute("SELECT * FROM states \
            WHERE name LIKE 'N%' \
            ORDER BY states.id ASC")
    rows = typed.fetchall()
    for row in rows:
        print(row)
