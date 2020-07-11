class CustomDictionary:

    def __init__(self, data=None):
        super(CustomDictionary, self).__init__()
        if data is not None:
            self._dict = dict(data)
        else:
            self._dict = dict()

    def __setitem__(self, key, item):
        self._dict[key] = item

    def __getitem__(self, key):
        return self._dict[key]

    def __len__(self):
        return len(self._dict)

    def __delitem__(self, key):
        del self._dict[key]

    def __str__(self):
        return str(self._dict)

    def __add__(self, other):
        new_dict = {}
        for key, value in self._dict.items():
            new_dict[key] = value
        for key, value in other._dict.items():
            new_dict[key] = value
        return new_dict

    def get(self, key):
        return self._dict[key]

    def keys(self):
        new_list = []
        for keys in self._dict:
            new_list.append(keys)
        return f'dict_keys({new_list})'

    def values(self):
        new_list = []
        for keys in self._dict:
            new_list.append(self._dict[keys])
        return f'dict_values({new_list})'

    def items(self):
        new_list = []
        for keys in self._dict:
            new_list.append((keys, self._dict[keys]))
        return f'dict_items({new_list})'


my_dict = CustomDictionary({'a': '1', 'b': '2'})
my_dict['c'] = '3'
print(my_dict)
other_dict = CustomDictionary({'fo': 'sho'})
print(my_dict + other_dict)
print(my_dict.items())
