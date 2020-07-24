from random import choice, randint


class Info:

    group_list = ['ABC-11', 'ABC-22', 'ABC-12', 'ABC-21', 'ABC-13', 'ABC-23', 'ABC-31', 'ABC-32', 'ABC-33']

    name_list = ['Sophia', 'Jacob', 'Isabella', 'Mason', 'Emma', 'William', 'Olivia', 'Jayden', 'Ava', 'Noah',
                 'Emily', 'Michael', 'Abigail', 'Ethan', 'Madison', 'Alexander', 'Mia', 'Aiden', 'Chloe', 'Daniel']

    second_name_list = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore',
                        'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia',
                        'Martinez', 'Robinson']

    faculty_list = ['Cybersecurity', 'IT', 'Telecommunications', 'Management']

    curator_list = ['Steven Spielberg', 'Alan Moore', 'Brad Pitt', 'Lionel Messi']

    @classmethod
    def create_valid_objects(cls, other):
        info_list = []
        for i in range(100):
            info_list.append({'name': (choice(cls.name_list) + ' ' + choice(cls.second_name_list)),
                              'rating': [randint(2, 5) for j in range(randint(3, 10))],
                              'group': choice(cls.group_list),
                              'curator': choice(cls.curator_list),
                              'faculty': choice(cls.faculty_list)})

            other.objects.create(name=info_list[i]['name'],
                                 rating=info_list[i]['rating'],
                                 group=info_list[i]['group'],
                                 curator=info_list[i]['curator'],
                                 faculty=info_list[i]['faculty'])

