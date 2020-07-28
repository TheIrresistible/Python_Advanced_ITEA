from random import choice, randint


class Info:
    category_list = ['Convenience Products', 'Shopping Products', 'Specialty Products', 'Emergency Products',
                     'Unsought Products']

    subcategory_list = ['Computers', 'Smartphones', 'Household appliances', 'Household goods', 'Plumbing']

    title_list = ['2u37ws6c', '56u6zkk5', 'tzisb3o3', 'zy5bpocr', 'yihrtvfb', 'jmu52h9s', 'w5vvvgj4', 'nw576pix',
                  '2itwmubw', 'xbjf38qu']

    @classmethod
    def create_post_objects(cls, other, category, subcategory):
        info_list = []
        for i in range(100):
            info_list.append({'title': choice(cls.title_list),
                              'category': choice(cls.category_list),
                              'subcategory': choice(cls.subcategory_list),
                              'price': randint(1, 2500),
                              'quantity': randint(1, 50)})

            category = category.objects.create(name=info_list[i]['category'])

            subcategory = subcategory.objects.create(name=info_list[i]['subcategory'],
                                                     category=category)

            other.objects.create(title=info_list[i]['title'],
                                 price=info_list[i]['price'],
                                 quantity=info_list[i]['quantity'],
                                 subcategory=subcategory,
                                 category=category)
