# Nome: Caio B B G de Toledo
# RA: 20.01430-9
class UserModel():
    def __init__(self, name, email, photo, password) -> None:
        self._name = name
        self._email = email
        self._photo = photo
        self._password = password

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_photo(self):
        return self._photo

    def get_password(self):
        return self._password
