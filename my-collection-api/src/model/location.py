from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .entity import Base

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    abrv = Column(String)

    def __init__(self, name, abrv):
        self.name = name
        self.abrv = abrv


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id