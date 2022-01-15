from marshmallow import fields
from marshmallow.schema import Schema
from sqlalchemy import Column, String, Integer
from .entity import Base


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    abrv = Column(String)

    def __init__(self, name, abrv):
        self.name = name
        self.abrv = abrv


class StateSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    abrv = fields.Str()
