from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float
from .entity import Entity, Base


class Item(Entity, Base): 
    __tablename__ = 'items'

    name = Column(String)
    artist = Column(String)
    purchased_price = Column(Float)
    model_number = Column(String)
    manufacturer = Column(String)
    sku = Column(String)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category")
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("City")
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")

    def __init__(self, name, artist, purchased_price, model_number, manufacturer, category_id, city_id, state_id, sku, description, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.artist = artist
        self.purchased_price = purchased_price
        self.manufacturer = manufacturer
        self.model_number = model_number
        self.sku = sku
        self.description = description
        self.category_id = category_id
        self.city_id = city_id
        self.state_id = state_id
