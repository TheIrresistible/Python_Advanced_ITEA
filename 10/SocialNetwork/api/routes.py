from flask import Flask
from flask_restful import Api
from .resources import PostResource, AuthorResource, TagResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PostResource, '/posts', '/posts/<post_id>')
api.add_resource(AuthorResource, '/authors', '/authors/<author_id>')
api.add_resource(TagResource, '/tags', '/tags/<tag_id>')
