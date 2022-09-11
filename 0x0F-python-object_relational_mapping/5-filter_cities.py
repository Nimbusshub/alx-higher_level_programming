#!/usr/bin/python3

"""A script that takes in user's input, filters it
and lists all cities of that state"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    condb = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    curs = condb.cursor()
    curs.execute("SELECT cities.name FROM cities\
            JOIN states ON cities.state_id=states.id\
            WHERE states.name LIKE %s", ("%" + sys.argv[4] + "%",))

    cities = curs.fetchall()
    List = []
    for city in cities:
        for char in city:
            List.append(char)
    print(", ".join(List))

    curs.close()
    condb.close()
