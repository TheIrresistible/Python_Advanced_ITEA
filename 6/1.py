class CustomList:

    def __init__(self, data=None):
        super(CustomList, self).__init__()
        if data is not None:
            self._list = list(data)
        else:
            self._list = list()

    def __len__(self):
        return len(self._list)

    def __getitem__(self, i):
        return self._list[i]

    def __delitem__(self, i):
        del self._list[i]

    def __setitem__(self, i, val):
        self._list[i] = val

    def __str__(self):
        return str(self._list)

    def __add__(self, other):
        return self._list + other._list

    def insert(self, i, val):
        self._list[i] = val

    def append(self, val):
        self._list = self._list + list('1')
        self._list[-1] = val

    def pop(self, i=-1):
        val = self._list[i]
        del self._list[i]
        return val

    def remove(self, val):
        for i in range(len(self._list)):
            if val == self._list[i]:
                del self._list[i]
                break

    def clear(self):
        for i in range(len(self._list)):
            del self._list[0]


my_list = CustomList([1, 'a', 2, 3, 4, 5])
my_list.append(7)
print(my_list)
a = my_list.pop()
print(a)
print(my_list)
my_list.remove(2)
print(my_list)
other_list = CustomList([1, 2])
print(my_list + other_list)