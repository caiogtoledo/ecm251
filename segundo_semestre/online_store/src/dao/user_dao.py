import sqlite3
from src.modules.login.models.user_model import UserModel


class UserDAO:

    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def get_user(self, user: UserModel) -> UserModel:
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM user
            WHERE email = '{user.get_email()}';
         """)
        responses = []
        for res in self.cursor.fetchall():
            responses.append(
                UserModel(
                    email=res[0],
                    name=res[1],
                    password=res[2],
                    photo=res[3]
                )
            )
        self.cursor.close()
        if len(responses) > 0:
            return responses[0]

    def add_user(self, user: UserModel):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO user (
                name,
                email,
                password,
                urlPic,
                isAdmin
            )
            VALUES(?,?,?,?,0);
        """, (
            user.get_name(),
            user.get_email(),
            user.get_password(),
            user.get_photo()
        ))
        self.conn.commit()
        self.cursor.close()

    def update_user(self, user: UserModel):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE user SET 
                name = '{user.get_name()}',
                email = {user.get_email()},
                urlPic = {user.get_photo()},
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
