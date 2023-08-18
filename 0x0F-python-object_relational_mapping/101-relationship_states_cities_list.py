#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State).order_by(State.id).all():
        print(f"{i.id}: {i.name}")
        for city in i.cities:
            print(f'\t{city.id}: {city.name}')

    for i in session.query(City).order_by(City.id).all():
        print(f"{i.state.name}")
