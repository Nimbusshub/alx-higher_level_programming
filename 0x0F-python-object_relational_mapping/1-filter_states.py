#!/usr/bin/python3

""" A script that lists all states starting with N """

if __name__ == '__main__':
    import MySQLdb
    import sys

condb = MySQLdb.connect(
    user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], port=3306)
curs = condb.cursor()
curs.execute("SELECT * FROM states")
states = curs.fetchall()

for state in states:
    if state[1].startswith('N'.upper()):
        print(state)

curs.close()
condb.close()
