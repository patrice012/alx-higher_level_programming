#!/usr/bin/python3

"""
Module contains script that prints
the first State object from the database hbtn_0e_6_usa
"""


def connect_db(host, port, username, passwd, db_name, **kwargs):
    """
    Use SQLAlchemy to connect to
    MySQL server running on localhost at port 330

    Args:
        host(str or int): Database host to use
        post(int): DB port
        user(str): DB user to use
        passwd(str): DB user's password
        db(str): database name to connect to

    Return:
        session(Session object): session object bind to our database
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if kwargs["dialect"] and kwargs["driver"]:
        dialect = kwargs["dialect"]
        driver = kwargs["driver"]
    else:
        dialect = "mysql"
        driver = "mysqldb"

    # create engine object
    arg = f"{dialect}+{driver}://{username}:{passwd}@{host}:{port}/{db_name}"
    engine = create_engine(
        arg,
        pool_pre_ping=True,
    )
    # create session object
    Session = sessionmaker(bind=engine)
    # bound sesion object to database
    session = Session()
    return session


def print_data(data):
    """
    Helper function used to print data
    """
    if data is None:
        print("Nothing")
    else:
        print("{}: {}".format(data.id, data.name))


def get_state(av):
    """
    Get the  first state in
    the database  using sqlalchemy ORM

    Args:
        av: list of arguments
    """
    from model_state import Base, State

    # get connection credentials
    host = "localhost"
    port = 3306
    user = av[0]
    passwd = av[1]
    db = av[2]
    kwargs = {"dialect": "mysql", "driver": "mysqldb"}

    # connect to database
    session = connect_db(host, port, user, passwd, db_name=db, **kwargs)
    # fetch data
    states = session.query(State).order_by(State.id).first()
    return states


if __name__ == "__main__":
    from sys import argv

    av = argv[1:]
    data = get_state(av)
    print_data(data)
