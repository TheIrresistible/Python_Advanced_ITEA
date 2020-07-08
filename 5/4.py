from datetime import date
import shelve


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


class User():

    all_posts = 'all_posts'

    def __init__(self, login):
        self.posts = 'posts'
        self.login = login

    def create_new_post(self, text):

        with shelve.open(self.posts) as p:
            p[f'{self.login}'] = f'{text}\n{date.today()}'
        with shelve.open(self.__class__.all_posts) as ap:
            ap[f'{self.login}'] = f'{text}\nCreated by {self.login} on {date.today()}'

    def show_posts(self):

        with shelve.open(self.posts) as p:
            for item in p:
                print(p[item])


class Administrator(User):

    def __init__(self, login):
        super().__init__(login)

    @staticmethod
    def show_users():
        with shelve.open(Registration.list_of_registrated) as lor:
            for item in lor:
                print(lor[item])

    @classmethod
    def show_posts(cls):
        with shelve.open(cls.all_posts) as ap:
            for item in ap:
                print(ap[item])


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
                action = input('1 - Create new post, 2 - Show posts, 3 - Exit from the account ')
                if action == '1':
                    text = input('Type in: ')
                    user1.create_new_post(text)

                if action == '2':
                    user1.show_posts()

                if action == '3':
                    break

                else:
                    continue

            if usr.role == 'Administrator':
                action = input('1 - Show users, 2 - Show posts, 3 - Exit from the account ')
                if action == '1':
                    user1.show_users()

                if action == '2':
                    user1.show_posts()

                if action == '3':
                    break

                else:
                    continue
