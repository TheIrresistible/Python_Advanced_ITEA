from datetime import date


class Registration:

    list_of_logins = ['vova']
    logpass = {'vova': '11q'}
    logrole = {'vova': 'Administrator'}
    list_of_registrated = [f'vova registrated {date.today()} as Administrator']

    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role

    @property
    def login(self):
        return self.login

    @login.setter
    def login(self, new):
        self.login = new

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, new):
        self.password = new

    @property
    def role(self):
        return self.role

    @role.setter
    def role(self, new):
        self.role = new

    def create_user(self):

        self.__class__.list_of_logins.append(self.login)
        self.__class__.list_of_registrated.append(f'{self.login} registrated {date.today()} as {self.role}')
        self.__class__.logpass[f'{self.login}'] = self.password

    @staticmethod
    def password_check(password):

        chars = set('0123456789$,!#@%^&*()_-=+`~')

        if any((c in chars) for c in password):
            return True
        else:
            return False

    @classmethod
    def login_check(cls, login):

        for i in cls.list_of_logins:
            if i == login:
                return False

        return True

    def login_into(self):
        if self.role == 'User':
            return User(self.login, [])
        if self.role == 'Administrator':
            return Administrator(self.login, [])
        else:
            return None


class Authorization(Registration):

    def __init__(self, login, password, role):
        super().__init__(login, password, role)
        self.role = self.__class__.logrole[self.login]

    def login_into(self):
        if self.role == 'User':
            return User(self.login, [])
        if self.role == 'Administrator':
            return Administrator(self.login, [])
        else:
            return None

    @classmethod
    def loginwithpass(cls, login, password):

        if login in cls.logpass:
            if cls.logpass[login] == password:
                return True

        return False


class User():

    all_posts = []

    def __init__(self, login, posts):
        self.posts = posts
        self.login = login

    @property
    def login(self):
        return self.login

    @login.setter
    def login(self, new):
        self.login = new

    def create_new_post(self, text):

        self.posts.append(f'{text}\n{date.today()}')
        self.__class__.all_posts.append(f'{text}\nCreated by {self.login} on {date.today()}')

    def show_posts(self):

        print(*self.posts, sep='\n')


class Administrator(User):

    def __init__(self, login, posts):
        super().__init__(login, posts)

    @staticmethod
    def show_users():
        for i in Registration.list_of_registrated:
            print(i)

    @classmethod
    def show_posts(cls):
        for i in cls.all_posts:
            print(i)


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

        try:
            usr = Authorization(log, password, Authorization.logrole[log])
        except KeyError:
            pass
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