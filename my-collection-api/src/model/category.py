from .entity import Base
from sqlalchemy import Column, String, Integer
from marshmallow import fields
from marshmallow.schema import Schema

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class CategorySchema(Schema):
    id = fields.Number()
    name = fields.Str()