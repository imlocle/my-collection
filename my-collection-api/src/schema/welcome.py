from marshmallow.schema import Schema
from marshmallow.fields import Str


class WelcomeSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["message"]

    message = Str()