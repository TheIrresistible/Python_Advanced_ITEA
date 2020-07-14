import sqlite3
import shelve
from datetime import date


class ConnManager:

    def __init__(self, db_name):

        self.db_name = db_name

    def __enter__(self):

        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.conn.close()
        if exc_val:
            raise


class Registration:

    logpass = 'logpass'
    logrole = 'logrole'
    list_of_registrated = 'list_of_registrated'

    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role

    def create_user(self):

        with shelve.open(self.list_of_registrated) as lor:
            lor[f'{self.login}'] = f'{self.login} registrated {date.today()} as {self.role}'

        with shelve.open(self.__class__.logpass) as lp:
            lp[f'{self.login}'] = self.password

        with shelve.open(self.__class__.logrole) as lr:
            lr[f'{self.login}'] = self.role

    @staticmethod
    def password_check(password):

        chars = set('0123456789$,!#@%^&*()_-=+`~')

        if any((c in chars) for c in password):
            return True
        else:
            return False

    @classmethod
    def login_check(cls, login):

        with shelve.open(cls.logpass) as lp:
            for i in lp:
                if i == login:
                    return False

        return True

    def login_into(self):
        if self.role == 'User':
            return User(self.login)
        if self.role == 'Administrator':
            return Administrator(self.login)
        else:
            return None


class Authorization(Registration):

    def __init__(self, login, password, role):
        super().__init__(login, password, role)
        with shelve.open(self.__class__.logrole) as lr:
            self.role = lr[self.login]

    def login_into(self):
        if self.role == 'User':
            return User(self.login)
        if self.role == 'Administrator':
            return Administrator(self.login)
        else:
            return None

    @classmethod
    def loginwithpass(cls, login, password):

        with shelve.open(cls.logpass) as lp:

            if login in lp:
                if lp[login] == password:
                    return True

        return False


class User:

    def __init__(self, login):
        self.login = login

    @staticmethod
    def get_excellent():
        with ConnManager('students.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Name, Surname, Ticket FROM Students '
                           'INNER JOIN Rating ON Students.id = Rating.student_id '
                           'WHERE ((Rating.Math + Rating.Physics + Rating.Philosophy)/3) >= 4.5')
            for i in cursor:
                print(*i)

    @staticmethod
    def get_all():
        with ConnManager('students.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Name, Surname, Ticket FROM Students')
            for i in cursor:
                print(*i)

    @staticmethod
    def get_by_ticket(ticket_num):
        with ConnManager('students.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Name, Surname FROM Students WHERE Ticket = ?', [ticket_num])
            for i in cursor:
                print(*i)

    @staticmethod
    def get_full_info(name, surname):
        with ConnManager('students.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT ((Rating.Math+Rating.Physics+Rating.Philosophy)/3), Faculties.Faculty, Ticket FROM Students '
                'INNER JOIN Faculties ON Students.Faculty = Faculties.faculty_id '
                'INNER JOIN Rating ON Students.id = Rating.student_id '
                'WHERE Students.Name = ? AND Students.Surname = ?', [name, surname])
            for i in cursor:
                print(*i)


class Administrator(User):

    def __init__(self, login):
        super().__init__(login)

    @staticmethod
    def new_student(name, surname, faculty, ticket):
        with ConnManager('students.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Students(Name, Surname, Faculty, Ticket) '
                           'VALUES(?, ?, ?, ?) ', [name, surname, faculty, ticket])
            conn.commit()

    @staticmethod
    def update_student(name, surname, column, info):
        with ConnManager('students.db') as conn:
            cursor = conn.cursor()
            if column == 'Faculty':
                all_f = {'Cybersecurity': 1, 'Telecommunications': 2, 'Management': 3}
                cursor.execute('UPDATE Students SET Faculty = ? WHERE Name = ? AND Surname = ? ',
                               [all_f[info], name, surname])

            elif column == 'Rating':
                cursor.execute(
                    'SELECT Rating.Math, Rating.Physics, Rating.Philosophy, Rating.student_id FROM Students '
                    'INNER JOIN Rating ON Students.id = Rating.student_id '
                    'WHERE Students.Name = ? AND Students.Surname = ?', [name, surname])
                rating_list = cursor.fetchone()
                print(f'Math: {rating_list[0]}. Physics: {rating_list[1]}. Philosophy: {rating_list[2]}')
                chose = input('Choose the subject: ')
                if chose == 'Math':
                    cursor.execute('UPDATE Rating SET Math = ? '
                                   'WHERE Rating.student_id = ? ', [info, rating_list[3]])
                elif chose == 'Physics':
                    cursor.execute('UPDATE Rating SET Physics = ? '
                                   'WHERE Rating.student_id = ? ', [info, rating_list[3]])
                elif chose == 'Philosophy':
                    cursor.execute('UPDATE Rating SET Philosophy = ? '
                                   'WHERE Rating.student_id = ? ', [info, rating_list[3]])

            conn.commit()


while True:

    lor = input('Do you have an account?  yes or no ')

    if lor == 'no':
        rol = input('Your role: ')
        if rol != 'User' and rol != 'Administrator':
            continue

        log = input('Login: ')

        if Registration.login_check(log) is False:
            print('Login is already exist')
            continue

        pass1 = input('Password: ')
        pass2 = input('Repeat password: ')

        if pass1 != pass2:
            print('Passwords are not the same')
            continue

        if Registration.password_check(pass1) is False:
            print('Password may contain numbers or specials')
            continue

        usr = Registration(log, pass1, rol)
        usr.create_user()
        print('Account is created')

    if lor == 'yes':
        log = input('Login: ')
        if Authorization.login_check(log) is True:
            print('Login does not exist')
            continue
        password = input('Password: ')

        if Authorization.loginwithpass(log, password) is False:
            print('Wrong password')
            continue

        with shelve.open(Authorization.logrole) as lr:
            usr = Authorization(log, password, lr[log])

        user1 = usr.login_into()
        print('You are logged in')

        while True:
            if usr.role == 'User':
                action = input('1 - Get excellent students, 2 - Get all students, 3 - Search by ticket, '
                               '4 -  Search by student, 5 - Exit from the account')
                if action == '1':
                    user1.get_excellent()

                if action == '2':
                    user1.get_all()

                if action == '3':
                    num = input('Enter ticket number: ')
                    user1.get_by_ticket(num)

                if action == '4':
                    n = input('Enter name: ')
                    s = input('Enter surname: ')
                    user1.get_full_info(n, s)

                if action == '5':
                    break

                else:
                    continue

            if usr.role == 'Administrator':
                action = input('1 - New student, 2 - Edit student, 3 - Exit from the account ')
                if action == '1':
                    name = input('Enter name: ')
                    surname = input('Enter surname: ')
                    faculty = input('Enter faculty: ')
                    ticket = input('Enter ticket: ')
                    user1.new_student(name, surname, faculty, ticket)

                if action == '2':
                    name = input('Enter name: ')
                    surname = input('Enter surname: ')
                    column = input('What do you want to change? (Faculty or Rating ')
                    info = input('Set new info: ')
                    user1.update_student(name, surname, column, info)

                if action == '3':
                    break

                else:
                    continue
