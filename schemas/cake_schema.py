from marshmallow import fields, Schema, ValidationError


class CakeSchema(Schema):

     Radius_cm = fields.Integer(required=True, data_key='Radius [cm]')
     Layers = fields.Integer(required=True)
     Topping = fields.String(required=True)


    # {
    #  "Price": 16,
    #  "Layers": 1,
    #  "Topping":"Picture",
    # }