from marshmallow import fields
from marshmallow.schema import Schema
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .entity import Base
from .state import StateSchema


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id


class CitySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    state = fields.Nested(StateSchema)
