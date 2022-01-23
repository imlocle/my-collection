from marshmallow import fields
from marshmallow.schema import Schema
from .location import CitySchema, StateSchema
from ..model.category import CategorySchema

class ItemSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    artist = fields.Str()
    purchased_price = fields.Float()
    manufacturer = fields.Str()
    model_number = fields.Str()
    category = fields.Nested(CategorySchema)
    city = fields.Nested(CitySchema)
    state = fields.Nested(StateSchema)
    sku = fields.Str()
    description = fields.Str()
    created_on = fields.DateTime()
    updated_on = fields.DateTime()
    last_updated_by = fields.Str()