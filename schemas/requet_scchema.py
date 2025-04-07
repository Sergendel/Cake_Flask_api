from marshmallow import fields, Schema, ValidationError

class RequestSchema(Schema):
    Pclass = fields.String(required=True)
    Sex = fields.String(required=True)
    Age = fields.String(required=True)
    SibSp = fields.String(required=True)
    Parch = fields.String(required=True)
    Fare = fields.String(required=True)
    Cabin = fields.String(required=True)
    Embarked = fields.String(required=True)