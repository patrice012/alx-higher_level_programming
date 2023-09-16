#!/usr/bin/python3

"""
Module contains script that deletes all State
objects with a name containing the letter a
from the database hbtn_0e_6_usa
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


def delete_states(av):
    """
    Deletes all State objects with a name
    containing the letter a from the database
    hbtn_0e_6_usa

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
    # search_params = av[3]
    kwargs = {"dialect": "mysql", "driver": "mysqldb"}

    # connect to database
    session = connect_db(host, port, user, passwd, db_name=db, **kwargs)
    # delete data
    """
    synchronize_session=fetch option:\
    'fetch' - Retrieves the primary key identity of affected rows by either\
    performing a SELECT before the UPDATE or DELETE, or by using RETURNING if\
    the database supports it, so that in-memory objects which are affected by\
    the operation can be refreshed with new values (updates) or expunged from\
    the Session (deletes)\
    Read more: https://docs.sqlalchemy.org/en/14/orm/session_basics.\
    html#selecting-a-synchronization-strategy
    """
    try:
        states = (
            session.query(State)
            .filter(State.name.ilike("%a%"))
            .delete(synchronize_session="fetch")
        )
        # commit changes
        session.commit()
    except TypeError as e:
        session.rollback()
        raise
    finally:
        session.close()  # optional, depends on use case


if __name__ == "__main__":
    from sys import argv

    av = argv[1:]
    delete_states(av)
