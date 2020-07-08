class File:

    def __init__(self, name, action):
        self.name = name
        self.action = action
        self.status = 1

    def __enter__(self):
        self.file = open(f'{self.name}', f'{self.action}')
        if self.status == 1:
            return self.file
        raise ValueError

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if exc_val == ValueError:
            print('You did something wrong with values')
        self.file.close()
        self.status = 0


with File('file.txt', 'w') as f:
    f.write('Hello world!')