#!/usr/bin/python3

""" A script that lists all states from database hbtn_0e_0_usa """
if __name__ == '__main__':
    import MySQLdb
    import sys

    condb = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], port=3306, db=sys.argv[3])
    curs = condb.cursor()
    curs.execute("SELECT * FROM states")
    states = curs.fetchall()
    for state in states:
        print(state)

    curs.close()
    condb.close()
