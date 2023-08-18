#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    ss = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for s in ss:
        print(f"{s.id}: {s.name}")
