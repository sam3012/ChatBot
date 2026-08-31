import sqlite3


class DB_OPERATION:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), 'ChatBot.db')
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tbl_users(
                username TEXT PRIMARY KEY,
                password TEXT
            );
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tbl_admins(
                username TEXT PRIMARY KEY,
                password TEXT
            );
            """
        )
        cursor.execute(
            """
            INSERT INTO tbl_admins (username, password)
            SELECT 'admin', 'admin'
            WHERE NOT EXISTS
            (
                SELECT username, password FROM tbl_admins
                WHERE username='admin' AND password='admin'
            )
            """
        )
        self.conn.commit()

    def user_check(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute(
            f'SELECT * FROM tbl_users WHERE username="{username}" AND password="{password}"')
        if len(cursor.fetchall()) > 0:
            return True
        else:
            return False

    def insert_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute(
            f'INSERT INTO tbl_users VALUES ("{username}" ,"{password}");')
        self.conn.commit()
        return True

    def admin_check(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute(
            f'SELECT * FROM tbl_admins WHERE username="{username}" AND password="{password}"')
        if len(cursor.fetchall()) > 0:
            return True
        else:
            return False
