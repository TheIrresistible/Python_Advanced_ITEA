import sqlite3


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


if __name__ == '__main__':
    with ConnManager('test.db') as conn:
        cursor = conn.cursor()
