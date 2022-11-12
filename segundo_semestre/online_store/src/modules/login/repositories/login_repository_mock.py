# Nome: Caio B B G de Toledo
# RA: 20.01430-9

class LoginRepositoryMock():
    login: str
    password: str

    def __init__(self) -> None:
        self._login_mock = 'caio'
        self._password_mock = 'senha'

    def check_login(self, login, password):
        if self._password_mock == password and self._login_mock == login:
            return True
        return False
