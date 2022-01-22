from sqlalchemy import Column, String, Integer, ForeignKey
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float
from .entity import Entity, Base
from .state import StateSchema
from .city import CitySchema


class Item(Entity, Base):
    __tablename__ = 'items'

    name = Column(String)
    purchased_price = Column(Float)
    sku = Column(String)
    description = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("City")
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")

    def __init__(self, name, purchased_price, city_id, state_id, sku, description, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.purchased_price = purchased_price
        self.city_id = city_id
        self.sku = sku
        self.description = description
        self.state_id = state_id


class ItemSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    purchased_price = fields.Float()
    city = fields.Nested(CitySchema)
    state = fields.Nested(StateSchema)
    sku = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
