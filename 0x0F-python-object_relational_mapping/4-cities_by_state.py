#!/usr/bin/python3

"""Lists all cities from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    condb = MySQLdb.connect(
        user=sys.argv[1], passwd="PassAlx1!!!", db=sys.argv[3], port=3306)
    curs = condb.cursor()
    curs.execute(
        "SELECT cities.id,cities.name,states.name FROM cities LEFT JOIN states ON cities.state_id=states.id")
    cities = curs.fetchall()

    for city in cities:
        print(city)

    curs.close()
    condb.close()
