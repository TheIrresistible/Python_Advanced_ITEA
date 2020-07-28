import mongoengine as me

me.connect('Shop')


class Category(me.Document):

    name = me.StringField(min_length=4, max_length=128, required=True)
    description = me.StringField(min_length=16, max_length=512)

    def __str__(self):
        return str(self.id)


class Subcategory(me.Document):

    name = me.StringField(min_length=4, max_length=128, required=True)
    description = me.StringField(min_length=16, max_length=512)
    category = me.ReferenceField(Category)

    def __str__(self):
        return str(self.id)


class Product(me.Document):

    title = me.StringField(min_length=4, max_length=256, required=True)
    price = me.FloatField(required=True)
    availability = me.BooleanField(default=True)
    quantity = me.IntField()
    views = me.IntField(default=0)
    subcategory = me.ReferenceField(Subcategory)
    category = me.ReferenceField(Category)
