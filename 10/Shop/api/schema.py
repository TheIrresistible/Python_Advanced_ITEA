from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(validate=validate.Length(min=4, max=256), required=True)
    price = fields.Float(required=True)
    availability = fields.Boolean()
    quantity = fields.Integer()
    views = fields.Integer(dump_only=True)
    subcategory = fields.String()
    category = fields.String()


class CategorySchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(validate=validate.Length(min=4, max=128), required=True)
    description = fields.String(validate=validate.Length(min=16, max=512))


class SubcategorySchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(validate=validate.Length(min=4, max=128), required=True)
    description = fields.String(validate=validate.Length(min=16, max=512))
    category = fields.String()
