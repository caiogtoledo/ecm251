# Nome: Caio B B G de Toledo
# RA: 20.01430-9

from src.dao.user_dao import UserDAO
from src.modules.login.models.user_model import UserModel
import streamlit as st


class LoginRepository():
    login: str
    password: str
    user_on_db: UserModel

    def __init__(self) -> None:
        pass

    def check_login(self, login, password):
        try:
            if len(login) > 0 and len(password) > 0:
                user_trying = UserModel(
                    email=login,
                    name=None,
                    photo=None,
                    password=password
                )
                user_on_db = UserDAO().get_user(user_trying)
                if user_on_db.get_password() == user_trying.get_password():
                    return True
            st.session_state["loginError"] = 'Login ou Senha inválidos'
            return False
        except:
            st.session_state["loginError"] = 'Login ou Senha inválidos'
            return False
