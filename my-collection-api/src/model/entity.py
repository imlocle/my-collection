from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..util.constant import SQLITE

engine = create_engine(SQLITE)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Entity():
    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime)
    updated_on = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_on = datetime.now()
        self.updated_on = datetime.now()
        self.last_updated_by = created_by
