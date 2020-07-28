from marshmallow import Schema, fields, validate


class PostSchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(validate=validate.Length(min=4, max=256), required=True)
    content = fields.String(validate=validate.Length(min=1, max=512), required=True)
    author = fields.String()
    created = fields.Date(dump_only=True)
    views = fields.Integer(dump_only=True)
    tag = fields.String()


class AuthorSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(validate=validate.Length(min=4, max=128), required=True)
    surname = fields.String(validate=validate.Length(min=4, max=128), required=True)
    number_of_posts = fields.Integer(dump_only=True)


class TagSchema(Schema):
    id = fields.String(dump_only=True)
    tag = fields.String(required=True)