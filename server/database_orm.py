from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

#connection string to sqlite database
#sqlalchemy_db_url = 'sqlite:///ibcollective.db'
sqlalchemy_db_url = 'sqlite:///importeddb.db'

#starting the engine
engine = create_engine(sqlalchemy_db_url)

#establishing engine session
SessionLocal = sessionmaker(bind=engine)

#initiation the communication class
Base = declarative_base()

#yielding the connection, so it can be closed once data is collected
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
