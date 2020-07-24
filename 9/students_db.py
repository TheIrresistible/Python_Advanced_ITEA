import mongoengine as me
from valid_module import Info


me.connect('students5_db')


class Student(me.Document):
    name = me.StringField(min_length=1, max_length=256, required=True)
    rating = me.ListField(me.IntField(min_length=1, max_length=1))
    group = me.StringField(min_length=1, max_length=256, required=True)
    curator = me.StringField(min_length=1, max_length=256, required=True)
    faculty = me.StringField(min_length=1, max_length=256, required=True)

    def __str__(self):
        return self.name

    @classmethod
    def excellent(cls, faculty):
        users = cls.objects.filter(faculty__in=[faculty])

        students = []
        for user in users:
            if sum(user.rating)/len(user.rating) > 4:

                students.append((user.name, user.group, user.curator, user.faculty))

        return students

    @classmethod
    def find_curator(cls, curator):
        users = cls.objects.filter(curator__in=[curator])

        students = []
        for user in users:
            students.append((user.name, user.group, user.curator, user.faculty))

        return students


if __name__ == '__main__':

    Info.create_valid_objects(Student)
    for i in Student.excellent('Management'):
        print(*i)
