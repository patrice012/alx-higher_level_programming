#!/usr/bin/python3

"""
Module contains script that takes in an argument
and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
1-Create database if not exist
2-populated db
3-run script cat 0-select_states.sql | mysql -uroot -p
4-run ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
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
    try:
        db = MySQLdb.connect(host, port=port, user=user, passwd=passwd, db=db)
    except MySQLdb.Error as e:
        # print(e)
        pass

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


def filter_user_data(av):
    """
    Get all states with a name matches the argument
    from the database  using MySQLdb connector

    Args:
        av: list of arguments
    """
    # get connection credentials
    host = "localhost"
    port = 3306
    user = av[0]
    passwd = av[1]
    db = av[2]
    search_param = av[3]

    # make connection to database
    cur, db = connect_db(host=host, port=port, user=user, passwd=passwd, db=db)

    # execute raw sql
    query = "SELECT * FROM states WHERE BINARY \
        name='{:s}' ORDER BY id ASC".format(
        search_param
    )
    states = []
    try:
        cur.execute(query)
        states = cur.fetchall()
    except MySQLdb.Error as e:
        # print(e)
        pass
    close_connection(cur, db)
    return states


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    av = argv[1:]
    data = filter_user_data(av)
    print_data(data)
