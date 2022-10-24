#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    typed = db.cursor()
    typed.execute("SELECT * FROM states")
    row = typed.fetchall()

    for rows in row:
        print(row)
