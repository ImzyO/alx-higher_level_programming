#!/usr/bin/python3
"""
Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
What? Empty?
Yes, it’s an SQL injection to delete all records of a table…
Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
from sys import
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,./
            passwd=argv[2], db=argv[3])
    with db.cursor() as typed:
        typed.execute("""SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY states.id ASC""",./
                {'name': argv[4]})

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
