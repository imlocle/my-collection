from marshmallow import fields
from marshmallow.schema import Schema

class StateSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    abrv = fields.Str()

class CitySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    state = fields.Nested(StateSchema)
