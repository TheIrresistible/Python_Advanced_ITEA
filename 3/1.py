class Dot:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y

    def set_y(self, new_y):
        self.x = new_y

    def get_z(self):
        return self.z

    def set_z(self, new_z):
        self.x = new_z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return(f'{x}, {y}, {z}')

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return(f'{x}, {y}, {z}')

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z

        return(f'{x}, {y}, {z}')

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z

        return(f'{x}, {y}, {z}')

first = Dot(1, 2, 3)
second = Dot(1, 5, 10)

print(first * second)
