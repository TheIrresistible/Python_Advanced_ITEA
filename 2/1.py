class Car:

    def __init__(self, fuel, power, volume):
        self.fuel = fuel
        self.power = power
        self.volume = volume

    def fuel(self):
        return self.fuel

    def power(self):
        return self.power

    def volume(self):
        return self.volume


class Truck(Car):

    def __init__(self, fuel, power, volume, color):
        self.fuel = fuel
        self.power = power
        self.volume = volume
        self.color = color

    def color(self):
        return self.color


class Passenger_car(Car):

    def __init__(self, fuel, power, volume, capacity):
        self.fuel = fuel
        self.power = power
        self.volume = volume
        self.capacity = capacity

    def load(self):
        return self.capacity
