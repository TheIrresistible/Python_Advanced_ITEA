from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from .models import Category, Subcategory, Product
from .schema import ProductSchema, SubcategorySchema, CategorySchema


class ProductResource(Resource):

    def get(self, product_id=None):
        if product_id:
            obj = Product.objects.get(id=product_id)
            obj.views += 1
            obj.save()
            return ProductSchema().dump(obj)
        else:
            result = Product.objects
            return ProductSchema().dump(result, many=True)

    def post(self):
        try:
            res = ProductSchema().load(request.get_json())
            obj = Product.objects.create(**res)
            return ProductSchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, product_id):
        try:
            res = ProductSchema().load(request.get_json())
            obj = Product.objects.get(id=product_id)
            obj.update(**res)
            return ProductSchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, product_id):
        Product.objects(id=product_id).delete()
        return {'status': 'deleted'}


class SubcategoryResource(Resource):
    def get(self, subcategory_id=None):
        if subcategory_id:
            obj = Product.objects.get(subcategory=subcategory_id)
            return ProductSchema().dump(obj)
        else:
            result = Subcategory.objects
            return SubcategorySchema().dump(result, many=True)

    def post(self):
        try:
            res = SubcategorySchema().load(request.get_json())
            obj = Subcategory.objects.create(**res)
            return SubcategorySchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, subcategory_id):
        try:
            res = SubcategorySchema().load(request.get_json())
            obj = Subcategory.objects.get(id=subcategory_id)
            obj.update(**res)
            return SubcategorySchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, subcategory_id):
        Subcategory.objects(id=subcategory_id).delete()
        return {'status': 'deleted'}


class CategoryResource(Resource):
    def get(self, category_id=None):
        if category_id:
            obj = Subcategory.objects.get(category=category_id)
            return SubcategorySchema().dump(obj)
        else:
            result = Category.objects
            return CategorySchema().dump(result, many=True)

    def post(self):
        try:
            res = CategorySchema().load(request.get_json())
            obj = Category.objects.create(**res)
            return CategorySchema().dump(obj)
        except ValidationError as err:
            return {'error': err.messages}

    def put(self, category_id):
        try:
            res = CategorySchema().load(request.get_json())
            obj = Category.objects.get(id=category_id)
            obj.update(**res)
            return CategorySchema().dump(obj.reload())
        except ValidationError as err:
            return {'error': err.messages}

    def delete(self, category_id):
        Category.objects(id=category_id).delete()
        return {'status': 'deleted'}


class AllProductsResource(Resource):

    def get(self):
        results = Product.objects.filter()
        obj = 0.0
        for result in results:
            obj = obj + result.price
        return obj

