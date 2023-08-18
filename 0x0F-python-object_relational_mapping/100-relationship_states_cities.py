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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    city = City(name="San Francisco", state=State(name="California"))
    session.add(city)
    session.commit()
