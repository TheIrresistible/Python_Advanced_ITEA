import mongoengine as me
import datetime

me.connect('Posts1')


class Author(me.Document):

    name = me.StringField(min_length=4, max_length=128, required=True)
    surname = me.StringField(min_length=4, max_length=128, required=True)
    number_of_posts = me.IntField(default=0)

    def __str__(self):
        return str(self.id)


class Tag(me.Document):

    tag = me.StringField(required=True)

    def __str__(self):
        return str(self.id)


class Post(me.Document):

    title = me.StringField(min_length=4, max_length=256, required=True)
    content = me.StringField(min_length=1, max_length=2048, required=True)
    created = me.DateField(default=datetime.date.today)
    author = me.ReferenceField(Author)
    views = me.IntField(default=0)
    tag = me.ReferenceField(Tag)


'''
if __name__ == '__main__':
    user1 = Author.objects.create(name='Ivan', surname='Drago', number_of_posts=1)
    user2 = Author.objects.create(name='Rocky', surname='Balboa', number_of_posts=1)

    tag1 = Tag.objects.create(tag='Hello')
    tag2 = Tag.objects.create(tag='World')

    post1 = Post.objects.create(title='Boxing', content='I love boxing', created=datetime.date(1985, 6, 25),
                                author=user2, views=0, tag=tag2)
    post2 = Post.objects.create(title='Boxing', content='I hate Rocky', created=datetime.date(1985, 6, 25),
                                author=user1, views=0, tag=tag1)
'''