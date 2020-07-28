from random import choice


class Info:
    title_list = ['The Old Guard', 'The Secret Life of Pets', '365 Days', 'The Kissing Booth', 'Fatal Affair',
                  'The Kissing Booth', 'The Kissing Booth']

    content_list = ['AWESOME!', 'What?', 'Genius Moves?', 'Leave Britney Alone', 'Awesome Soccer Skills',
                    'Tim Burton Look', 'Evolution of Dance', 'Bobcat Freestyle Video', 'workout tips',
                    'weight lifting advice']

    tag_list = ['#love', '#photooftheday', '#fashion', '#beautiful', '#happy', '#cute', '#selfie', '#summer', '#art',
                '#friends', '#nature', '#fun', '#smile', '#food', '#family']

    name_list = ['Sophia', 'Jacob', 'Isabella', 'Mason', 'Emma', 'William', 'Olivia', 'Jayden', 'Ava', 'Noah',
                 'Emily', 'Michael', 'Abigail', 'Ethan', 'Madison', 'Alexander', 'Mia', 'Aiden', 'Chloe', 'Daniel']

    second_name_list = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore',
                        'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia',
                        'Martinez', 'Robinson']


    @classmethod
    def create_post_objects(cls, other, author, tag):
        info_list = []
        for i in range(100):
            info_list.append({'title': choice(cls.title_list),
                              'content': choice(cls.content_list),
                              'tag': choice(cls.tag_list),
                              'name': choice(cls.name_list),
                              'surname': choice(cls.second_name_list)})

            author = author.objects.create(name=info_list[i]['name'],
                                           surname=info_list[i]['surname'])

            tag = tag.objects.create(tag=info_list[i]['tag'])

            other.objects.create(title=info_list[i]['title'],
                                 content=info_list[i]['content'],
                                 author=author,
                                 tag=tag)
