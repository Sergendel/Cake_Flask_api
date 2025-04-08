from marshmallow import fields, Schema, ValidationError


class ToppingSchema(Schema):

    Radius_cm = fields.Integer(required=True, data_key='Radius [cm]')
    Layers = fields.Integer(required=True)