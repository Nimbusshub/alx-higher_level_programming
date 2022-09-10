#!/usr/bin/python3

""" A script that lists all states from database hbtn_0e_0_usa """

import MySQLdb
import sys
condb = MySQLdb.connect(username=sys.argv[0], passwd=sys.argv[1], port=3306, db=sys.argv[2])
curs = db.cursor()
curs.execute("SELECT %s, %s FROM states ORDER BY id ASC", (id, state,))
print(curs.fetchone())
