#!/usr/bin/python3

"""
Module contains script that lists all states from the database hbtn_0e_0_usa
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
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)

    # create cursor object
    cur = db.cursor()
    return cur


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
    username = av[0]
    password = av[1]
    db_name = av[2]

    # make connection to database
    cur = connect_db(host, port, user=username, passwd=password, db=db_name)

    # execute raw sql
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    return states


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    av = argv[1:]
    data = get_all_data(av)
    print_data(data)
