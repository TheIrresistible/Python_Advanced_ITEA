import mongoengine as me

me.connect('lesson_db')


class Telegram(me.Document):
    name = me.StringField(min_length=4, max_length=512, required=True)
    number = me.StringField(required=True)
    mail = me.StringField(min_length=4, max_length=512, required=True)
    location = me.StringField(min_length=4, max_length=256, required=True)
    wishes = me.StringField(min_length=1, max_length=1024)

    def __str__(self):
        return str(self.id)



