from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from .models import Author, Tag, Post
from .schema import PostSchema, AuthorSchema, TagSchema


class PostResource(Resource):

    def get(self, post_id=None):
        if post_id:
            obj = Post.objects.get(id=post_id)
            obj.views += 1
            obj.save()
            return PostSchema().dump(obj)
        else:
            result = Post.objects
            return PostSchema().dump(result, many=True)

    def post(self):
        try:
            res = PostSchema().load(request.get_json())
            obj = Post.objects.create(**res)
            a_obj = Author.objects.get(id=obj.author)
            a_obj.number_of_posts += 1
            a_obj.save()
            return PostSchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, post_id):
        try:
            res = PostSchema().load(request.get_json())
            obj = Post.objects.get(id=post_id)
            obj.update(**res)
            return PostSchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, post_id):
        Post.objects(id=post_id).delete()
        return {'status': 'deleted'}


class AuthorResource(Resource):
    def get(self, author_id=None):
        if author_id:
            obj = Post.objects.get(author=author_id)
            return PostSchema().dump(obj)
        else:
            result = Author.objects
            return AuthorSchema().dump(result, many=True)

    def post(self):
        try:
            res = AuthorSchema().load(request.get_json())
            obj = Author.objects.create(**res)
            return AuthorSchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, author_id):
        try:
            res = AuthorSchema().load(request.get_json())
            obj = Author.objects.get(id=author_id)
            obj.update(**res)
            return AuthorSchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, author_id):
        Author.objects(id=author_id).delete()
        return {'status': 'deleted'}


class TagResource(Resource):
    def get(self, tag_id=None):
        if tag_id:
            obj = Post.objects.get(tag=tag_id)
            return PostSchema().dump(obj)
        else:
            result = Tag.objects
            return TagSchema().dump(result, many=True)

    def post(self):
        try:
            res = TagSchema().load(request.get_json())
            obj = Tag.objects.create(**res)
            return TagSchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, tag_id):
        try:
            res = TagSchema().load(request.get_json())
            obj = Tag.objects.get(id=tag_id)
            obj.update(**res)
            return TagSchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, tag_id):
        Tag.objects(id=tag_id).delete()
        return {'status': 'deleted'}
