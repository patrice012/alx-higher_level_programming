#!/usr/bin/python3

"""
Module contains script that lists all states
from the database hbtn_0e_0_usa
1-Create database if not exist
2-populated db
3-run script cat 0-select_states.sql | mysql -uroot -p
"""


def connect_db(host, port, user, passwd, db, **kwargs):
    """
    Connect MySQLdb to a Database

    Args:
        host(str or int): Database host to use
        post(int): DB port
        user(str): DB user to use
        passwd(str): DB user's password
        db(str): database name to connect to

    Return:
        cur(cursor): cursor object
    """
    db = MySQLdb.connect(host, port=port, user=user, passwd=passwd, db=db)

    # create cursor object
    cur = db.cursor()
    return cur, db


def close_connection(*args):
    """
    Make clean up. Close all opening connection
    eg: cursor
    """
    for value in args:
        value.close()


def print_data(datas):
    """
    Helper function used to print data
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
    user = av[0]
    passwd = av[1]
    db = av[2]

    # make connection to database
    cur, db = connect_db(host=host, port=port, user=user, passwd=passwd, db=db)

    # execute raw sql
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    states = cur.fetchall()
    close_connection(cur, db)
    return states


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    av = argv[1:]
    data = get_all_data(av)
    print_data(data)
