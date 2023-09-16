#!/usr/bin/python3

"""
Module contains script that takes in the name
of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""


def connect_db(host, port, user, passwd, db_name, **kwargs):
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
    arg = (host, user, passwd, db_name)
    try:
        db = MySQLdb.connect(*arg, port=port)
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
    print(", ".join(datas))


def get_cities(av):
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
    search_params = av[3]

    # connect to database
    cur, db = connect_db(host, port, user=user, passwd=passwd, db_name=db)

    # execute raw sql
    # """
    # SELECT cities.name FROM states
    # INNER JOIN cities ON states.id = cities.state_id
    # WHERE states.name = %s
    # ORDER BY cities.id ASC
    # """
    rows = "cities.name"
    tables = "cities"
    condition = f"cities.state_id = (SELECT id FROM states WHERE name = %s)"
    order = "cities.id"
    query = f"""
    SELECT {rows}
    FROM {tables}
    WHERE {condition}
    ORDER BY {order}
    """
    states = []
    try:
        cur.execute(query, (search_params,))
        states = cur.fetchall()
    except MySQLdb.Error as e:
        print(e)
        pass
    close_connection(cur, db)
    return [state[0] for state in states]


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    av = argv[1:]
    data = get_cities(av)
    print_data(data)
