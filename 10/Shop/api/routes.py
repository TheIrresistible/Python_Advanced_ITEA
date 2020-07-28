from flask import Flask
from flask_restful import Api
from .resources import ProductResource, CategoryResource, SubcategoryResource, AllProductsResource

app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, '/categories', '/categories/<category_id>')
api.add_resource(SubcategoryResource, '/subcategories', '/subcategories/<subcategory_id>')
api.add_resource(ProductResource, '/products', '/products/<product_id>')
api.add_resource(AllProductsResource, '/allproducts')
