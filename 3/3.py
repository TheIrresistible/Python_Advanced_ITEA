class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


print('--------------Stack--------------')
s = Stack()
s.push('hello')
s.push('world')
print(s.peek())
print(s.size())
print(s.pop())
print(s.size())


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


print('--------------Queue--------------')
q = Queue()
q.enqueue('dog')
q.enqueue('cat')
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())
print(q.size())

class Complex:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def _complex(self):

        return (f'{self.first} + {self.second}j')

    def __add__(self, other):
        first = self.first + other.first
        second = self.second + other.second
        if second < 0:
            return (f'{first} - {abs(second)}j')
        else:
            return (f'{first} + {second}j')

    def __sub__(self, other):
        first = self.first - other.first
        second = self.second - other.second
        if second < 0:
            return(f'{first} - {abs(second)}j')
        else:
            return (f'{first} + {second}j')

    def __mul__(self, other):
        first = self.first * other.first
        second = self.second * other.second
        if second < 0:
            return (f'{first} - {abs(second)}j')
        else:
            return (f'{first} + {second}j')

    def __truediv__(self, other):
        first = self.first / other.first
        second = self.second / other.second
        if second < 0:
            return (f'{first} - {abs(second)}j')
        else:
            return (f'{first} + {second}j')


print('-------------Complex-------------')
first_number = Complex(10, 15)
second_number = Complex(5, 20)

print(first_number._complex())
print(first_number - second_number)
print(first_number / second_number)


