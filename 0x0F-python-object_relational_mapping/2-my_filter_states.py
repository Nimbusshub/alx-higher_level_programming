#!/usr/bin/python3

"""A script that takes an argument and displays all the values
in the states table of hbtn_0e_0_usa database
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    condb = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], port=3306, db=sys.argv[3])
    curs = condb.cursor()
    curs.execute("SELECT * FROM states\
        WHERE CONVERT(`name` USING latin1)\
        COLLATE Latin1_General_CS = '{input}'".format(input=sys.argv[4]))

    states = curs.fetchall()
    for state in states:
        print(state)

    curs.close()
    condb.close()
