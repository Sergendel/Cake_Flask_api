from marshmallow import fields, Schema, ValidationError


class CakeSchema(Schema):
     Layers = fields.Integer(required=True)
     Topping = fields.String(required=True)
     Price = fields.Integer(required=True)

    # {
    #  "Layers": 1,
    #  "Topping":"Picture",
    #  "Price": 311
    # }