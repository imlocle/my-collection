from sqlalchemy import Column, String
from marshmallow import Schema, fields
from sqlalchemy.sql.sqltypes import Float
from .entity import Entity, Base


class Item(Entity, Base):
    __tablename__ = 'Items'

    name = Column(String)
    purchased_price = Column(Float)
    location = Column(String)
    sku = Column(String)
    description = Column(String)

    def __init__(self, name, purchased_price, location, sku, description, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.purchased_price = purchased_price
        self.location = location
        self.sku = sku
        self.description = description


class ItemSchema(Schema):
    id = fields.Number()
    name = fields.String()
    purchased_price = fields.Float()
    location = fields.String()
    sku = fields.String()
    description = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.String()
