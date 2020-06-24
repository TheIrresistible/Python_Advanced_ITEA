class Dot:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self, new_x):
        self._x = new_x

    def get_y(self):
        return self._y

    def set_y(self, new_y):
        self._x = new_y

    def get_z(self):
        return self._z

    def set_z(self, new_z):
        self._x = new_z

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        z = self._z + other._z

        return Dot(x, y, z)

    def __sub__(self, other):
        x = self._x - other._x
        y = self._y - other._y
        z = self._z - other._z
        
        return Dot(x, y, z)

    def __mul__(self, other):
        x = self._x * other._x
        y = self._y * other._y
        z = self._z * other._z

        return Dot(x, y, z)

    def __truediv__(self, other):
        x = self._x / other._x
        y = self._y / other._y
        z = self._z / other._z

        return Dot(x, y, z)

first = Dot(1, 2, 3)
second = Dot(1, 5, 10)
third = Dot(2, 5, 14)

res = first + second * third
print(res._x, res._y, res._z)
