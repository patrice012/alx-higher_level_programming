#!/usr/bin/python3

"""
Module contains script that lists all states from the database hbtn_0e_0_usa
"""


def connect_db(host, port, user, passwd, db, **kwargs):
    """
    Connect MySQLdb to a Database

    Return:
        cur(cursor): cursor object
    """
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)

    # create cursor object
    cur = db.cursor()
    return cur


def print_data(datas):
    """
    Helper function use to print data
    """
    for data in datas:
        print(data)


def get_all_data(av):
    """
    Get all state in DB using MySQLdb connector
    """
    # get connection credentials
    host = "localhost"
    port = 3306
    username = av[0]
    password = av[1]
    db_name = av[2]

    # make connection to database
    cur = connect_db(host, port, user=username, passwd=password, db=db_name)

    # execute raw sql
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()
    return states


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    av = argv[1:]
    data = get_all_data(av)
    print_data(data)
