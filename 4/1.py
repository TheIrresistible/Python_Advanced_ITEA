from datetime import date
from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, surname, year, month, day, faculty):
        self.surname = surname
        self.year = year
        self.month = month
        self.day = day
        self.faculty = faculty

    @abstractmethod
    def print_info(self):
        today = date.today()
        age = today.year - self.year - ((today.month, today.day) < (self.month, self.day))
        print(f'Surname: {self.surname}\n'
              f'Date of birth: {self.day}.{self.month}.{self.year}\n'
              f'Age: {age}\n'
              f'Faculty: {self.faculty}')


class Entrant(Person):

    def __init__(self, surname, year, month, day, faculty):
        super().__init__(surname, year, month, day, faculty)

    def print_info(self):
        today = date.today()
        age = today.year - self.year - ((today.month, today.day) < (self.month, self.day))
        print(f'Surname: {self.surname}\n'
              f'Date of birth: {self.day}.{self.month}.{self.year}\n'
              f'Age: {age}\n'
              f'Faculty: {self.faculty}')


class Student(Person):

    def __init__(self, surname, year, month, day, faculty, course):
        super().__init__(surname, year, month, day, faculty)
        self.course = course

    def print_info(self):
        today = date.today()
        age = today.year - self.year - ((today.month, today.day) < (self.month, self.day))
        print(f'Surname: {self.surname}\n'
              f'Date of birth: {self.day}.{self.month}.{self.year}\n'
              f'Age: {age}\n'
              f'Faculty: {self.faculty}\n'
              f'Course: {self.course}')


class Teacher(Person):

    def __init__(self, surname, year, month, day, faculty, position, experience):
        super().__init__(surname, year, month, day, faculty)
        self.position = position
        self.experience = experience

    def print_info(self):
        today = date.today()
        age = today.year - self.year - ((today.month, today.day) < (self.month, self.day))
        print(f'Surname: {self.surname}\n'
              f'Date of birth: {self.day}.{self.month}.{self.year}\n'
              f'Age: {age}\n'
              f'Faculty: {self.faculty}\n'
              f'Position: {self.position}\n'
              f'Experience: {self.experience}')


all_list = []
list_of_years = []

n = int(input("Enter the number of persons: "))

for i in range(n):

    person = int(input('Who are you? 1) Entrant, 2) Student, 3) Teacher '))

    if person != 1 and person != 2 and person != 3:
        continue

    name = input('Enter your Surname: ')
    day, month, year = [int(x) for x in input("Enter the date of birth: ").split('.')]

    if person == 1:
        faculty = input('Enter faculty: ')
        entrant = Entrant(name, year, month, day, faculty)
        entrant.print_info()
        all_list.append(Entrant(name, year, month, day, faculty))

    if person == 2:
        faculty = input('Enter faculty: ')
        course = input('Enter course: ')
        stud = Student(name, year, month, day, faculty, course)
        stud.print_info()
        all_list.append(Student(name, year, month, day, faculty, course))

    if person == 3:
        faculty = input('Enter faculty: ')
        position = input('Enter position: ')
        experience = input('Enter work experience: ')
        teach = Teacher(name, year, month, day, faculty, position, experience)
        teach.print_info()
        all_list.append(Teacher(name, year, month, day, faculty, position, experience))

    ls = [name, year]
    list_of_years.append(ls)

print('\nDatabase:')
for i in all_list:
    print(i.print_info())

print('\nNext will be selected persons whose year of birth falls within a given period')

d1 = int(input('Enter the beginning of the period: '))
d2 = int(input('Enter the ending of the period: '))
print('\nPersons satisfying a given condition: ')

for i in range(n):
    if (list_of_years[i][1] >= d1) and (list_of_years[i][1] <= d2):
        print(list_of_years[i][0])